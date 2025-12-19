# UsageQuota


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **float** |  | 
**period** | **str** |  | 

## Example

```python
from attachmentav.models.usage_quota import UsageQuota

# TODO update the JSON string below
json = "{}"
# create an instance of UsageQuota from a JSON string
usage_quota_instance = UsageQuota.from_json(json)
# print the JSON string representation of the object
print(UsageQuota.to_json())

# convert the object into a dict
usage_quota_dict = usage_quota_instance.to_dict()
# create an instance of UsageQuota from a dict
usage_quota_from_dict = UsageQuota.from_dict(usage_quota_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


