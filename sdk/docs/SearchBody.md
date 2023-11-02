# SearchBody

DTO representing the search query

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**with_path** | **str** | Optional path field to limit the search to result with a matching (case insensitive) path | [optional] 
**name** | **str** | Name of the file or folder to be searched | 

## Example

```python
from lusid_drive.models.search_body import SearchBody

# TODO update the JSON string below
json = "{}"
# create an instance of SearchBody from a JSON string
search_body_instance = SearchBody.from_json(json)
# print the JSON string representation of the object
print SearchBody.to_json()

# convert the object into a dict
search_body_dict = search_body_instance.to_dict()
# create an instance of SearchBody from a dict
search_body_form_dict = search_body.from_dict(search_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


