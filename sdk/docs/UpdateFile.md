# UpdateFile

DTO representing the update of the name or path of a file

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | Path of the updated file | 
**name** | **str** | Name of the updated file | 

## Example

```python
from lusid_drive.models.update_file import UpdateFile

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFile from a JSON string
update_file_instance = UpdateFile.from_json(json)
# print the JSON string representation of the object
print UpdateFile.to_json()

# convert the object into a dict
update_file_dict = update_file_instance.to_dict()
# create an instance of UpdateFile from a dict
update_file_form_dict = update_file.from_dict(update_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


