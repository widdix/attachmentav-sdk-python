import attachmentav

configuration = attachmentav.Configuration()
# When using the SaaS offering
configuration.api_key['apiKeyAuth'] = "<API_KEY_PLACEHOLDER>"
# When using the self-hosted offering, replace attachmentav.yourcompany.com with the domain name of your attachmentAV API installation: https://attachmentav.com/help/virus-malware-scan-api-aws/developer/definition.html#domain-name
#configuration.access_token = "<API_KEY_PLACEHOLDER>"
#configuration.host = "https://attachmentav.yourcompany.com/api/v1"

with attachmentav.ApiClient(configuration) as api_client:
  api_instance = attachmentav.AttachmentAVApi(api_client)

sync_s3_scan_request = attachmentav.SyncS3ScanRequest(
  bucket = "<BUCKET_NAME_PLACEHOLDER>",
  key = "<OBJECT_KEY_PLACEHOLDER>"
)
scan_result = api_instance.scan_sync_s3_post(sync_s3_scan_request)
print(scan_result)
