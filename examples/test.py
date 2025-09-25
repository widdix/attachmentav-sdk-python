import os
import attachmentav
from attachmentav.rest import ApiException
from pprint import pprint


configuration = attachmentav.Configuration(
  host = "https://eu.developer.attachmentav.com/v1"
)
configuration.api_key['apiKeyAuth'] = os.environ["ATTACHMENTAV_API_KEY"]

with attachmentav.ApiClient(configuration) as api_client:
  api_instance = attachmentav.AttachmentAVApi(api_client)


  # print(open("README.md", "r").read())

  with open("README.md", "rb") as file:
    file_content = file.read()
    scan_result = api_instance.scan_sync_binary_post(file_content)
    print(scan_result)

  sync_download_scan_request = attachmentav.SyncDownloadScanRequest(
    download_url = "https://cloudonaut.io/images/2025/07/step-by-step@540w2x.webp"
  )
  scan_result = api_instance.scan_sync_download_post(sync_download_scan_request)
  print(scan_result)

  sync_s3_scan_request = attachmentav.SyncS3ScanRequest(
    bucket = "bucketav-release-data",
    key = "latest.json"
  )
  scan_result = api_instance.scan_sync_s3_post(sync_s3_scan_request)
  print(scan_result)

  async_download_scan_request = attachmentav.AsyncDownloadScanRequest(
    download_url = "https://cloudonaut.io/images/2025/07/step-by-step@540w2x.webp",
    callback_url = "https://example.com/callback"
  )
  api_instance.scan_async_download_post(async_download_scan_request)
  
  async_s3_scan_request = attachmentav.AsyncS3ScanRequest(
    bucket = "bucketav-release-data",
    key = "latest.json",
    callback_url = "https://example.com/callback"
  )
  api_instance.scan_async_s3_post(async_s3_scan_request)