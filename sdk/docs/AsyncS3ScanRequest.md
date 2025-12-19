# AsyncS3ScanRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket** | **str** |  | 
**key** | **str** |  | 
**version** | **str** |  | [optional] 
**callback_url** | **str** |  | [optional] 
**callback_headers** | **Dict[str, str]** |  | [optional] 
**trace_id** | **str** |  | [optional] 
**custom_data** | **str** |  | [optional] 

## Example

```python
from attachmentav.models.async_s3_scan_request import AsyncS3ScanRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncS3ScanRequest from a JSON string
async_s3_scan_request_instance = AsyncS3ScanRequest.from_json(json)
# print the JSON string representation of the object
print(AsyncS3ScanRequest.to_json())

# convert the object into a dict
async_s3_scan_request_dict = async_s3_scan_request_instance.to_dict()
# create an instance of AsyncS3ScanRequest from a dict
async_s3_scan_request_from_dict = AsyncS3ScanRequest.from_dict(async_s3_scan_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


