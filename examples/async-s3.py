import attachmentav

configuration = attachmentav.Configuration()
configuration.api_key['apiKeyAuth'] = "<API_KEY_PLACEHOLDER>"

with attachmentav.ApiClient(configuration) as api_client:
  api_instance = attachmentav.AttachmentAVApi(api_client)

async_s3_scan_request = attachmentav.AsyncS3ScanRequest(
  bucket = "<BUCKET_NAME_PLACEHOLDER>",
  key = "<OBJECT_KEY_PLACEHOLDER>",
  callback_url = "https://api.yourcompany.com/attachmentav/callback"
)
api_instance.scan_async_s3_post(async_s3_scan_request)
print("Async S3 submitted")
