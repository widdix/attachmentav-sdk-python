import attachmentav
import sys
import time
import uuid

configuration = attachmentav.Configuration()
configuration.api_key['apiKeyAuth'] = "<API_KEY_PLACEHOLDER>"

with attachmentav.ApiClient(configuration) as api_client:
  api_instance = attachmentav.AttachmentAVApi(api_client)

trace_id = str(uuid.uuid4())

async_s3_scan_request = attachmentav.AsyncS3ScanRequest(
  bucket = "<BUCKET_NAME_PLACEHOLDER>",
  key = "<OBJECT_KEY_PLACEHOLDER>",
  trace_id = trace_id
)
api_instance.scan_async_s3_post(async_s3_scan_request)
print("Async S3 submitted. Start to poll for scan result...")

i = 0
while True:
  print('.');
  try:
    scan_result = api_instance.scan_async_result_get(trace_id)
    print(scan_result)
    sys.exit(0)
  except attachmentav.exceptions.NotFoundException:
    i += 1
    if i < 10:
      time.sleep(5)
    else:
      print('Async download scan result not found')
      sys.exit(1)
