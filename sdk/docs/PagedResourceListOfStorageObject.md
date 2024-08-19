# PagedResourceListOfStorageObject


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[StorageObject]**](StorageObject.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid_drive.models.paged_resource_list_of_storage_object import PagedResourceListOfStorageObject

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResourceListOfStorageObject from a JSON string
paged_resource_list_of_storage_object_instance = PagedResourceListOfStorageObject.from_json(json)
# print the JSON string representation of the object
print PagedResourceListOfStorageObject.to_json()

# convert the object into a dict
paged_resource_list_of_storage_object_dict = paged_resource_list_of_storage_object_instance.to_dict()
# create an instance of PagedResourceListOfStorageObject from a dict
paged_resource_list_of_storage_object_form_dict = paged_resource_list_of_storage_object.from_dict(paged_resource_list_of_storage_object_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


