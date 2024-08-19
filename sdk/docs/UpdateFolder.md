# UpdateFolder

DTO representing the update of the name or path of a file

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | Path of the updated folder | 
**name** | **str** | Name of the updated folder | 

## Example

```python
from lusid_drive.models.update_folder import UpdateFolder

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFolder from a JSON string
update_folder_instance = UpdateFolder.from_json(json)
# print the JSON string representation of the object
print UpdateFolder.to_json()

# convert the object into a dict
update_folder_dict = update_folder_instance.to_dict()
# create an instance of UpdateFolder from a dict
update_folder_form_dict = update_folder.from_dict(update_folder_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


