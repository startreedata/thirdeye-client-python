# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from thirdeye_client.configuration import Configuration


class NotificationSpecApiModel(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'type': 'str',
        'params': 'dict(str, object)'
    }

    attribute_map = {
        'type': 'type',
        'params': 'params'
    }

    def __init__(self, type=None, params=None, _configuration=None):  # noqa: E501
        """NotificationSpecApiModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._type = None
        self._params = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if params is not None:
            self.params = params

    @property
    def type(self):
        """Gets the type of this NotificationSpecApiModel.  # noqa: E501


        :return: The type of this NotificationSpecApiModel.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NotificationSpecApiModel.


        :param type: The type of this NotificationSpecApiModel.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def params(self):
        """Gets the params of this NotificationSpecApiModel.  # noqa: E501


        :return: The params of this NotificationSpecApiModel.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this NotificationSpecApiModel.


        :param params: The params of this NotificationSpecApiModel.  # noqa: E501
        :type: dict(str, object)
        """

        self._params = params

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(NotificationSpecApiModel, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NotificationSpecApiModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NotificationSpecApiModel):
            return True

        return self.to_dict() != other.to_dict()
