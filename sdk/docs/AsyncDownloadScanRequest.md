# AsyncDownloadScanRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download_url** | **str** |  | 
**download_headers** | **Dict[str, str]** |  | [optional] 
**callback_url** | **str** |  | [optional] 
**callback_headers** | **Dict[str, str]** |  | [optional] 
**trace_id** | **str** |  | [optional] 
**custom_data** | **str** |  | [optional] 

## Example

```python
from attachmentav.models.async_download_scan_request import AsyncDownloadScanRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncDownloadScanRequest from a JSON string
async_download_scan_request_instance = AsyncDownloadScanRequest.from_json(json)
# print the JSON string representation of the object
print(AsyncDownloadScanRequest.to_json())

# convert the object into a dict
async_download_scan_request_dict = async_download_scan_request_instance.to_dict()
# create an instance of AsyncDownloadScanRequest from a dict
async_download_scan_request_from_dict = AsyncDownloadScanRequest.from_dict(async_download_scan_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


