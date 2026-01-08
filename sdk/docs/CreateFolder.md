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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

path: StrictStr = "example_path"
name: StrictStr = "example_name"
create_folder_instance = CreateFolder(path=path, name=name)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

