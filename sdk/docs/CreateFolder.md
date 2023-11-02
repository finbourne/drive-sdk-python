# CreateFolder

DTO representing the creation of a folder

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | Path of the created folder | 
**name** | **str** | Name of the created folder | 

## Example

```python
from lusid_drive.models.create_folder import CreateFolder

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFolder from a JSON string
create_folder_instance = CreateFolder.from_json(json)
# print the JSON string representation of the object
print CreateFolder.to_json()

# convert the object into a dict
create_folder_dict = create_folder_instance.to_dict()
# create an instance of CreateFolder from a dict
create_folder_form_dict = create_folder.from_dict(create_folder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


