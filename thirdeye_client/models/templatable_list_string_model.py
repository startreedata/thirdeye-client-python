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


class TemplatableListStringModel(object):
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
        'templated_value': 'str',
        'value': 'list[str]'
    }

    attribute_map = {
        'templated_value': 'templatedValue',
        'value': 'value'
    }

    def __init__(self, templated_value=None, value=None, _configuration=None):  # noqa: E501
        """TemplatableListStringModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._templated_value = None
        self._value = None
        self.discriminator = None

        if templated_value is not None:
            self.templated_value = templated_value
        if value is not None:
            self.value = value

    @property
    def templated_value(self):
        """Gets the templated_value of this TemplatableListStringModel.  # noqa: E501


        :return: The templated_value of this TemplatableListStringModel.  # noqa: E501
        :rtype: str
        """
        return self._templated_value

    @templated_value.setter
    def templated_value(self, templated_value):
        """Sets the templated_value of this TemplatableListStringModel.


        :param templated_value: The templated_value of this TemplatableListStringModel.  # noqa: E501
        :type: str
        """

        self._templated_value = templated_value

    @property
    def value(self):
        """Gets the value of this TemplatableListStringModel.  # noqa: E501


        :return: The value of this TemplatableListStringModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this TemplatableListStringModel.


        :param value: The value of this TemplatableListStringModel.  # noqa: E501
        :type: list[str]
        """

        self._value = value

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
        if issubclass(TemplatableListStringModel, dict):
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
        if not isinstance(other, TemplatableListStringModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TemplatableListStringModel):
            return True

        return self.to_dict() != other.to_dict()
