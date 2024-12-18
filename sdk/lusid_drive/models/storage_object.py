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

from datetime import datetime
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictInt, StrictStr, conlist, constr, validator, Field
from lusid_drive.models.link import Link

class StorageObject(BaseModel):
    """
    An object representation of a drive file or folder  # noqa: E501
    """
    id: constr(strict=True) = Field(...,alias="id", description="File or folder identifier") 
    path: constr(strict=True) = Field(...,alias="path", description="Path of the folder or file") 
    name: constr(strict=True) = Field(...,alias="name", description="Name of the folder or file") 
    created_by: constr(strict=True) = Field(...,alias="createdBy", description="Identifier of the user who created the file or folder") 
    created_on: datetime = Field(..., alias="createdOn", description="Date of file/folder creation")
    updated_by: constr(strict=True) = Field(...,alias="updatedBy", description="Identifier of the last user to modify the file or folder") 
    updated_on: datetime = Field(..., alias="updatedOn", description="Date of file/folder modification")
    type: constr(strict=True) = Field(...,alias="type", description="Type of storage object (file or folder)") 
    size: Optional[StrictInt] = Field(None, description="Size of the file in bytes")
    status: constr(strict=True) = Field(None,alias="status", description="File status corresponding to virus scan status.  (Active, Available, Checking, MalwareDetected, Failed)") 
    status_detail: constr(strict=True) = Field(None,alias="statusDetail", description="Detailed description describing any negative terminal state of file") 
    links: Optional[conlist(Link)] = None
    __properties = ["id", "path", "name", "createdBy", "createdOn", "updatedBy", "updatedOn", "type", "size", "status", "statusDetail", "links"]

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
    def from_json(cls, json_str: str) -> StorageObject:
        """Create an instance of StorageObject from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        # set to None if size (nullable) is None
        # and __fields_set__ contains the field
        if self.size is None and "size" in self.__fields_set__:
            _dict['size'] = None

        # set to None if status (nullable) is None
        # and __fields_set__ contains the field
        if self.status is None and "status" in self.__fields_set__:
            _dict['status'] = None

        # set to None if status_detail (nullable) is None
        # and __fields_set__ contains the field
        if self.status_detail is None and "status_detail" in self.__fields_set__:
            _dict['statusDetail'] = None

        # set to None if links (nullable) is None
        # and __fields_set__ contains the field
        if self.links is None and "links" in self.__fields_set__:
            _dict['links'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> StorageObject:
        """Create an instance of StorageObject from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return StorageObject.parse_obj(obj)

        _obj = StorageObject.parse_obj({
            "id": obj.get("id"),
            "path": obj.get("path"),
            "name": obj.get("name"),
            "created_by": obj.get("createdBy"),
            "created_on": obj.get("createdOn"),
            "updated_by": obj.get("updatedBy"),
            "updated_on": obj.get("updatedOn"),
            "type": obj.get("type"),
            "size": obj.get("size"),
            "status": obj.get("status"),
            "status_detail": obj.get("statusDetail"),
            "links": [Link.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None
        })
        return _obj
