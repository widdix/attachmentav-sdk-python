# SyncDownloadScanRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download_url** | **str** |  | 
**download_headers** | **Dict[str, str]** |  | [optional] 

## Example

```python
from attachmentav.models.sync_download_scan_request import SyncDownloadScanRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SyncDownloadScanRequest from a JSON string
sync_download_scan_request_instance = SyncDownloadScanRequest.from_json(json)
# print the JSON string representation of the object
print(SyncDownloadScanRequest.to_json())

# convert the object into a dict
sync_download_scan_request_dict = sync_download_scan_request_instance.to_dict()
# create an instance of SyncDownloadScanRequest from a dict
sync_download_scan_request_from_dict = SyncDownloadScanRequest.from_dict(sync_download_scan_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


