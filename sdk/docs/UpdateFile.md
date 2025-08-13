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
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, constr, validator

path: StrictStr = "example_path"
name: StrictStr = "example_name"
update_file_instance = UpdateFile(path=path, name=name)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

