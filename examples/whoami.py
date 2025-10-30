import attachmentav

configuration = attachmentav.Configuration()
configuration.api_key['apiKeyAuth'] = "<API_KEY_PLACEHOLDER>"

with attachmentav.ApiClient(configuration) as api_client:
  api_instance = attachmentav.AttachmentAVApi(api_client)

whoami_result = api_instance.whoami_get()
print(whoami_result)
