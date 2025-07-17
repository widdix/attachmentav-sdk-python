# attachmentav.AttachmentAVApi

All URIs are relative to *https://eu.developer.attachmentav.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**scan_async_download_post**](AttachmentAVApi.md#scan_async_download_post) | **POST** /scan/async/download | 
[**scan_async_s3_post**](AttachmentAVApi.md#scan_async_s3_post) | **POST** /scan/async/s3 | 
[**scan_sync_binary_post**](AttachmentAVApi.md#scan_sync_binary_post) | **POST** /scan/sync/binary | 
[**scan_sync_download_post**](AttachmentAVApi.md#scan_sync_download_post) | **POST** /scan/sync/download | 
[**scan_sync_s3_post**](AttachmentAVApi.md#scan_sync_s3_post) | **POST** /scan/sync/s3 | 


# **scan_async_download_post**
> scan_async_download_post(async_download_scan_request)

Download a file from a remote location (HTTP/HTTPS), scan the file, and post the scan result to your callback URL.

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer Authentication (bearerAuth):

```python
import attachmentav
from attachmentav.models.async_download_scan_request import AsyncDownloadScanRequest
from attachmentav.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu.developer.attachmentav.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = attachmentav.Configuration(
    host = "https://eu.developer.attachmentav.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = attachmentav.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with attachmentav.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = attachmentav.AttachmentAVApi(api_client)
    async_download_scan_request = attachmentav.AsyncDownloadScanRequest() # AsyncDownloadScanRequest | 

    try:
        api_instance.scan_async_download_post(async_download_scan_request)
    except Exception as e:
        print("Exception when calling AttachmentAVApi->scan_async_download_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **async_download_scan_request** | [**AsyncDownloadScanRequest**](AsyncDownloadScanRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scan_async_s3_post**
> scan_async_s3_post(async_s3_scan_request)

Download a file from S3, scan the file, and post the scan result to your callback URL. A bucket policy is required to grant attachmentAV access to the S3 objects.

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer Authentication (bearerAuth):

```python
import attachmentav
from attachmentav.models.async_s3_scan_request import AsyncS3ScanRequest
from attachmentav.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu.developer.attachmentav.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = attachmentav.Configuration(
    host = "https://eu.developer.attachmentav.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = attachmentav.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with attachmentav.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = attachmentav.AttachmentAVApi(api_client)
    async_s3_scan_request = attachmentav.AsyncS3ScanRequest() # AsyncS3ScanRequest | 

    try:
        api_instance.scan_async_s3_post(async_s3_scan_request)
    except Exception as e:
        print("Exception when calling AttachmentAVApi->scan_async_s3_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **async_s3_scan_request** | [**AsyncS3ScanRequest**](AsyncS3ScanRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scan_sync_binary_post**
> ScanResult scan_sync_binary_post(body)

Upload a file, scan the file, and return the scan result.

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer Authentication (bearerAuth):

```python
import attachmentav
from attachmentav.models.scan_result import ScanResult
from attachmentav.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu.developer.attachmentav.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = attachmentav.Configuration(
    host = "https://eu.developer.attachmentav.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = attachmentav.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with attachmentav.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = attachmentav.AttachmentAVApi(api_client)
    body = None # bytearray | 

    try:
        api_response = api_instance.scan_sync_binary_post(body)
        print("The response of AttachmentAVApi->scan_sync_binary_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttachmentAVApi->scan_sync_binary_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **bytearray**|  | 

### Return type

[**ScanResult**](ScanResult.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scan_sync_download_post**
> ScanResult scan_sync_download_post(sync_download_scan_request)

Download a file from a remote location (HTTP/HTTPS), scan the file, and return the scan result.

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer Authentication (bearerAuth):

```python
import attachmentav
from attachmentav.models.scan_result import ScanResult
from attachmentav.models.sync_download_scan_request import SyncDownloadScanRequest
from attachmentav.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu.developer.attachmentav.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = attachmentav.Configuration(
    host = "https://eu.developer.attachmentav.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = attachmentav.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with attachmentav.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = attachmentav.AttachmentAVApi(api_client)
    sync_download_scan_request = attachmentav.SyncDownloadScanRequest() # SyncDownloadScanRequest | 

    try:
        api_response = api_instance.scan_sync_download_post(sync_download_scan_request)
        print("The response of AttachmentAVApi->scan_sync_download_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttachmentAVApi->scan_sync_download_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sync_download_scan_request** | [**SyncDownloadScanRequest**](SyncDownloadScanRequest.md)|  | 

### Return type

[**ScanResult**](ScanResult.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scan_sync_s3_post**
> ScanResult scan_sync_s3_post(sync_s3_scan_request)

Download a file from S3, scan the file, and return the scan result. A bucket policy is required to grant attachmentAV access to the S3 objects.

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer Authentication (bearerAuth):

```python
import attachmentav
from attachmentav.models.scan_result import ScanResult
from attachmentav.models.sync_s3_scan_request import SyncS3ScanRequest
from attachmentav.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu.developer.attachmentav.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = attachmentav.Configuration(
    host = "https://eu.developer.attachmentav.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = attachmentav.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with attachmentav.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = attachmentav.AttachmentAVApi(api_client)
    sync_s3_scan_request = attachmentav.SyncS3ScanRequest() # SyncS3ScanRequest | 

    try:
        api_response = api_instance.scan_sync_s3_post(sync_s3_scan_request)
        print("The response of AttachmentAVApi->scan_sync_s3_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttachmentAVApi->scan_sync_s3_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sync_s3_scan_request** | [**SyncS3ScanRequest**](SyncS3ScanRequest.md)|  | 

### Return type

[**ScanResult**](ScanResult.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

