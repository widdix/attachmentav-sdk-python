# CallbackFailures


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failures** | [**List[CallbackFailure]**](CallbackFailure.md) |  | 
**next_cursor** | **str** |  | [optional] 

## Example

```python
from attachmentav.models.callback_failures import CallbackFailures

# TODO update the JSON string below
json = "{}"
# create an instance of CallbackFailures from a JSON string
callback_failures_instance = CallbackFailures.from_json(json)
# print the JSON string representation of the object
print(CallbackFailures.to_json())

# convert the object into a dict
callback_failures_dict = callback_failures_instance.to_dict()
# create an instance of CallbackFailures from a dict
callback_failures_from_dict = CallbackFailures.from_dict(callback_failures_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


