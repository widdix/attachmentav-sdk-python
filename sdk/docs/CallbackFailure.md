# CallbackFailure


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**time** | **datetime** |  | 
**download_url** | **str** |  | 
**callback_url** | **str** |  | 
**error_json** | **str** |  | 

## Example

```python
from attachmentav.models.callback_failure import CallbackFailure

# TODO update the JSON string below
json = "{}"
# create an instance of CallbackFailure from a JSON string
callback_failure_instance = CallbackFailure.from_json(json)
# print the JSON string representation of the object
print(CallbackFailure.to_json())

# convert the object into a dict
callback_failure_dict = callback_failure_instance.to_dict()
# create an instance of CallbackFailure from a dict
callback_failure_from_dict = CallbackFailure.from_dict(callback_failure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


