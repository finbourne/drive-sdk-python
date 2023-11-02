# StorageObject

An object representation of a drive file or folder

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | File or folder identifier | 
**path** | **str** | Path of the folder or file | 
**name** | **str** | Name of the folder or file | 
**created_by** | **str** | Identifier of the user who created the file or folder | 
**created_on** | **datetime** | Date of file/folder creation | 
**updated_by** | **str** | Identifier of the last user to modify the file or folder | 
**updated_on** | **datetime** | Date of file/folder modification | 
**type** | **str** | Type of storage object (file or folder) | 
**size** | **int** | Size of the file in bytes | [optional] 
**status** | **str** | File status corresponding to virus scan status.  (Active, Available, Checking, MalwareDetected, Failed) | [optional] 
**status_detail** | **str** | Detailed description describing any negative terminal state of file | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid_drive.models.storage_object import StorageObject

# TODO update the JSON string below
json = "{}"
# create an instance of StorageObject from a JSON string
storage_object_instance = StorageObject.from_json(json)
# print the JSON string representation of the object
print StorageObject.to_json()

# convert the object into a dict
storage_object_dict = storage_object_instance.to_dict()
# create an instance of StorageObject from a dict
storage_object_form_dict = storage_object.from_dict(storage_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


