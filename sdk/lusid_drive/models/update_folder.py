# coding: utf-8

"""
    FINBOURNE Drive API

    FINBOURNE Technology  # noqa: E501

    Contact: info@finbourne.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, constr, validator, Field

class UpdateFolder(BaseModel):
    """
    DTO representing the update of the name or path of a file  # noqa: E501
    """
    path: constr(strict=True) = Field(...,alias="path", description="Path of the updated folder") 
    name: constr(strict=True) = Field(...,alias="name", description="Name of the updated folder") 
    __properties = ["path", "name"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def __str__(self):
        """For `print` and `pprint`"""
        return pprint.pformat(self.dict(by_alias=False))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> UpdateFolder:
        """Create an instance of UpdateFolder from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UpdateFolder:
        """Create an instance of UpdateFolder from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UpdateFolder.parse_obj(obj)

        _obj = UpdateFolder.parse_obj({
            "path": obj.get("path"),
            "name": obj.get("name")
        })
        return _obj
