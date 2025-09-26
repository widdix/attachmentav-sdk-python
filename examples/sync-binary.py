import attachmentav

configuration = attachmentav.Configuration()
configuration.api_key['apiKeyAuth'] = "<API_KEY_PLACEHOLDER>"

with attachmentav.ApiClient(configuration) as api_client:
  api_instance = attachmentav.AttachmentAVApi(api_client)

with open("/path/to/file", "rb") as file:
    file_content = file.read()
    scan_result = api_instance.scan_sync_binary_post(file_content)
    print(scan_result)
