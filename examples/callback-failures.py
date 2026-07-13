import attachmentav

configuration = attachmentav.Configuration()
configuration.api_key['apiKeyAuth'] = "<API_KEY_PLACEHOLDER>"

with attachmentav.ApiClient(configuration) as api_client:
  api_instance = attachmentav.AttachmentAVApi(api_client)

callback_failures = api_instance.callback_failures_get('https://api.yourcompany.com/attachmentav/callback')
print(callback_failures)
