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
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, constr, validator

with_path: Optional[StrictStr] = "example_with_path"
name: StrictStr = "example_name"
search_body_instance = SearchBody(with_path=with_path, name=name)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

