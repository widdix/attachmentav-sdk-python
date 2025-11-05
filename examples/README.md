An [active subscription and API key](https://attachmentav.com/help/virus-malware-scan-api/setup-guide/#api-key) is required. Replace `<API_KEY_PLACEHOLDER>` with your API key.

```bash
pip3 install attachmentav-virus-malware-scan-sdk

python3 sync-download.py
python3 sync-binary.py
python3 sync-s3.py

python3 async-download.py
python3 async-s3.py

pip3 install cryptography
python3 verify-callback.py # Replace <CALLBACK_URL_PLACEHOLDER> as described in the code.

python3 whoami.py
python3 usage.py
```
