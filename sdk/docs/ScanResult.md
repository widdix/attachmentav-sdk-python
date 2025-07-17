# ScanResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**finding** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**realfiletype** | **str** |  | [optional] 

## Example

```python
from attachmentav.models.scan_result import ScanResult

# TODO update the JSON string below
json = "{}"
# create an instance of ScanResult from a JSON string
scan_result_instance = ScanResult.from_json(json)
# print the JSON string representation of the object
print(ScanResult.to_json())

# convert the object into a dict
scan_result_dict = scan_result_instance.to_dict()
# create an instance of ScanResult from a dict
scan_result_from_dict = ScanResult.from_dict(scan_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


