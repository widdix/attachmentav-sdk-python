import attachmentav

configuration = attachmentav.Configuration()
configuration.api_key['apiKeyAuth'] = "<API_KEY_PLACEHOLDER>"

with attachmentav.ApiClient(configuration) as api_client:
  api_instance = attachmentav.AttachmentAVApi(api_client)

async_download_scan_request = attachmentav.AsyncDownloadScanRequest(
  download_url = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
  callback_url = "https://api.yourcompany.com/attachmentav/callback"
)
api_instance.scan_async_download_post(async_download_scan_request)
print("Async download submitted")
