import attachmentav

configuration = attachmentav.Configuration()
configuration.api_key['apiKeyAuth'] = "<API_KEY_PLACEHOLDER>"

with attachmentav.ApiClient(configuration) as api_client:
  api_instance = attachmentav.AttachmentAVApi(api_client)

sync_download_scan_request = attachmentav.SyncDownloadScanRequest(
  download_url = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"
)
scan_result = api_instance.scan_sync_download_post(sync_download_scan_request)
print(scan_result)
