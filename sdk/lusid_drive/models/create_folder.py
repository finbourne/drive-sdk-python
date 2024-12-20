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
from pydantic.v1 import BaseModel, Field, constr, validator

class CreateFolder(BaseModel):
    """
    DTO representing the creation of a folder  # noqa: E501
    """
    path: constr(strict=True, max_length=512, min_length=1) = Field(..., description="Path of the created folder")
    name: constr(strict=True, max_length=50, min_length=1) = Field(..., description="Name of the created folder")
    __properties = ["path", "name"]

    @validator('path')
    def path_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[\/a-zA-Z0-9 \-_]+$", value):
            raise ValueError(r"must validate the regular expression /^[\/a-zA-Z0-9 \-_]+$/")
        return value

    @validator('name')
    def name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[A-Za-z0-9_-]+[A-Za-z0-9 _-]*$", value):
            raise ValueError(r"must validate the regular expression /^[A-Za-z0-9_-]+[A-Za-z0-9 _-]*$/")
        return value

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
    def from_json(cls, json_str: str) -> CreateFolder:
        """Create an instance of CreateFolder from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateFolder:
        """Create an instance of CreateFolder from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateFolder.parse_obj(obj)

        _obj = CreateFolder.parse_obj({
            "path": obj.get("path"),
            "name": obj.get("name")
        })
        return _obj
