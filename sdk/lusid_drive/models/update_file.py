# coding: utf-8

"""
    FINBOURNE Drive API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.636
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from lusid_drive.configuration import Configuration


class UpdateFile(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'path': 'str',
        'name': 'str'
    }

    attribute_map = {
        'path': 'path',
        'name': 'name'
    }

    required_map = {
        'path': 'required',
        'name': 'required'
    }

    def __init__(self, path=None, name=None, local_vars_configuration=None):  # noqa: E501
        """UpdateFile - a model defined in OpenAPI"
        
        :param path:  Path of the updated file (required)
        :type path: str
        :param name:  Name of the updated file (required)
        :type name: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._path = None
        self._name = None
        self.discriminator = None

        self.path = path
        self.name = name

    @property
    def path(self):
        """Gets the path of this UpdateFile.  # noqa: E501

        Path of the updated file  # noqa: E501

        :return: The path of this UpdateFile.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this UpdateFile.

        Path of the updated file  # noqa: E501

        :param path: The path of this UpdateFile.  # noqa: E501
        :type path: str
        """
        if self.local_vars_configuration.client_side_validation and path is None:  # noqa: E501
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                path is not None and len(path) > 512):
            raise ValueError("Invalid value for `path`, length must be less than or equal to `512`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                path is not None and len(path) < 1):
            raise ValueError("Invalid value for `path`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                path is not None and not re.search(r'^[\/a-zA-Z0-9 \-_]+$', path)):  # noqa: E501
            raise ValueError(r"Invalid value for `path`, must be a follow pattern or equal to `/^[\/a-zA-Z0-9 \-_]+$/`")  # noqa: E501

        self._path = path

    @property
    def name(self):
        """Gets the name of this UpdateFile.  # noqa: E501

        Name of the updated file  # noqa: E501

        :return: The name of this UpdateFile.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateFile.

        Name of the updated file  # noqa: E501

        :param name: The name of this UpdateFile.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 256):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and not re.search(r'^[A-Za-z0-9_\-\.]+[A-Za-z0-9_\-\. ]*$', name)):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^[A-Za-z0-9_\-\.]+[A-Za-z0-9_\-\. ]*$/`")  # noqa: E501

        self._name = name

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateFile):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateFile):
            return True

        return self.to_dict() != other.to_dict()
