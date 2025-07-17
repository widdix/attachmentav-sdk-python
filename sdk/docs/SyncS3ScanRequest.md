# SyncS3ScanRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket** | **str** |  | 
**key** | **str** |  | 
**version** | **str** |  | [optional] 

## Example

```python
from attachmentav.models.sync_s3_scan_request import SyncS3ScanRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SyncS3ScanRequest from a JSON string
sync_s3_scan_request_instance = SyncS3ScanRequest.from_json(json)
# print the JSON string representation of the object
print(SyncS3ScanRequest.to_json())

# convert the object into a dict
sync_s3_scan_request_dict = sync_s3_scan_request_instance.to_dict()
# create an instance of SyncS3ScanRequest from a dict
sync_s3_scan_request_from_dict = SyncS3ScanRequest.from_dict(sync_s3_scan_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


