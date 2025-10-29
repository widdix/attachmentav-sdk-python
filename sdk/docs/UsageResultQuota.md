# UsageResultQuota


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **float** |  | [optional] 
**period** | **str** |  | [optional] 

## Example

```python
from attachmentav.models.usage_result_quota import UsageResultQuota

# TODO update the JSON string below
json = "{}"
# create an instance of UsageResultQuota from a JSON string
usage_result_quota_instance = UsageResultQuota.from_json(json)
# print the JSON string representation of the object
print(UsageResultQuota.to_json())

# convert the object into a dict
usage_result_quota_dict = usage_result_quota_instance.to_dict()
# create an instance of UsageResultQuota from a dict
usage_result_quota_from_dict = UsageResultQuota.from_dict(usage_result_quota_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


