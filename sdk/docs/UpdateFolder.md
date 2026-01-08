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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

path: StrictStr = "example_path"
name: StrictStr = "example_name"
update_folder_instance = UpdateFolder(path=path, name=name)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

