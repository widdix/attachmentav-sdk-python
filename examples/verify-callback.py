import http.server
import socketserver
import sys
import threading
import time
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
import attachmentav

SIGNATURE_TOLERANCE_IN_MILLIS = 5 * 60 * 1000

API_KEY = '<API_KEY_PLACEHOLDER>'

# To make your server running on localhost accessible from the Internet, we recommend to use ngrok.
# 1. Install and configure it as described here: https://ngrok.com/docs/getting-started
# 2. In your terminal, run:
# ngrok http 8081
# 3. Insert the ngrok URL (e.g. https://42d3a8497f95.ngrok-free.app) below:
CALLBACK_URL = '<CALLBACK_URL_PLACEHOLDER>'

PUBLIC_KEY_PEM = """-----BEGIN RSA PUBLIC KEY-----
MIIBCgKCAQEAyLoZzjo1cQV9ZN2TH/alrxWiQ3u/ndT0HMrLMdBTVO3Tz1nUjLt6
SqKZsN8dQhvPoEjfyhCTEg7MPWopG3n0cf3NRxtoeXy/Z62b1zdUd426kMuKOQP8
Yy6cxa/RtK2tkHCnTGxjfvNmMK+m68sFmsilR88LnIN71my4cG8bIDGDftWublvK
AEOWhxSECYn1XEtyrQL5lm8HFnHdE9ys56xTJkdr5Mmkvanrnd/hXzTHzjruGcLv
bjciI82+Z335AzYgJcnmH4/zsBuyPL2FJSfQF9NsPaTJuQgkw1usAKBQcujcEriY
UDNWgTe1a+LOnCEMb+9mAYw8lMRYRd3CBwIDAQAB
-----END RSA PUBLIC KEY-----"""

configuration = attachmentav.Configuration()
configuration.api_key['apiKeyAuth'] = API_KEY

with attachmentav.ApiClient(configuration) as api_client:
  api_instance = attachmentav.AttachmentAVApi(api_client)

whoami_result = api_instance.whoami_get()
TENANT_ID = whoami_result.tenant_id # the tenant_id never changes. we recommend to hard code it to avoid yet another HTTPS call.
# TENANT_ID = '<TENANT_ID_PLACEHOLDER>'

def verify(unixtime_in_millis, public_key_pem, timestamp, tenant_id, callback_url, body, signature):
    """Verify the signature of the callback request."""
    try:
        public_key = serialization.load_pem_public_key(
            public_key_pem.encode(),
            backend=default_backend()
        )
        message = f"{timestamp}.{tenant_id}.{callback_url}.{body}".encode()
        signature_bytes = bytes.fromhex(signature)
        
        try:
            public_key.verify(
                signature_bytes,
                message,
                padding.PKCS1v15(),
                hashes.SHA256()
            )
        except Exception:
            return False
        
        return abs(unixtime_in_millis - int(timestamp)) <= SIGNATURE_TOLERANCE_IN_MILLIS
    except Exception as e:
        print(f"Verification error: {e}", file=sys.stderr)
        return False


class CallbackHandler(http.server.BaseHTTPRequestHandler):
    """HTTP request handler for the callback server."""
    
    def do_POST(self):
        """Handle POST requests."""
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length).decode('utf-8')
        
        timestamp = self.headers.get('x-timestamp', '')
        signature = self.headers.get('x-signature', '')
        
        if verify(int(time.time() * 1000), PUBLIC_KEY_PEM, timestamp, TENANT_ID, CALLBACK_URL, body, signature):
            self.send_response(204)
            self.end_headers()
            print('Received valid callback', body, file=sys.stderr)
        else:
            self.send_response(403)
            self.end_headers()
            print('Received invalid callback', body)
        
        threading.Thread(target=self.server.shutdown).start()
    
    def log_message(self, format, *args):
        """Suppress default logging."""
        pass


def start_server():
    """Start the HTTP server to listen for callbacks."""
    with socketserver.TCPServer(("", 8081), CallbackHandler) as httpd:
        httpd.serve_forever()


server_thread = threading.Thread(target=start_server, daemon=True)
server_thread.start()

async_download_scan_request = attachmentav.AsyncDownloadScanRequest(
  download_url = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
  callback_url = CALLBACK_URL
)
api_instance.scan_async_download_post(async_download_scan_request)
print('Async download submitted')

server_thread.join()
