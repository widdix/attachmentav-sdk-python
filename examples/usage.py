import attachmentav

configuration = attachmentav.Configuration()
configuration.api_key['apiKeyAuth'] = "<API_KEY_PLACEHOLDER>"

with attachmentav.ApiClient(configuration) as api_client:
  api_instance = attachmentav.AttachmentAVApi(api_client)

usage_result = api_instance.usage_get()
print(usage_result)
