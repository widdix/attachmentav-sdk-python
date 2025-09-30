import attachmentav

configuration = attachmentav.Configuration()
configuration.api_key['apiKeyAuth'] = "<API_KEY_PLACEHOLDER>"

with attachmentav.ApiClient(configuration) as api_client:
  api_instance = attachmentav.AttachmentAVApi(api_client)

sync_s3_scan_request = attachmentav.SyncS3ScanRequest(
  bucket = "<BUCKET_NAME_PLACEHOLDER>",
  key = "<OBJECT_KEY_PLACEHOLDER>"
)
scan_result = api_instance.scan_sync_s3_post(sync_s3_scan_request)
print(scan_result)
