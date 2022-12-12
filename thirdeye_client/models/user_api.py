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


class UserApi(object):
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
        'id': 'int',
        'principal': 'str',
        'created': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'principal': 'principal',
        'created': 'created'
    }

    def __init__(self, id=None, principal=None, created=None, _configuration=None):  # noqa: E501
        """UserApi - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._principal = None
        self._created = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if principal is not None:
            self.principal = principal
        if created is not None:
            self.created = created

    @property
    def id(self):
        """Gets the id of this UserApi.  # noqa: E501


        :return: The id of this UserApi.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserApi.


        :param id: The id of this UserApi.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def principal(self):
        """Gets the principal of this UserApi.  # noqa: E501


        :return: The principal of this UserApi.  # noqa: E501
        :rtype: str
        """
        return self._principal

    @principal.setter
    def principal(self, principal):
        """Sets the principal of this UserApi.


        :param principal: The principal of this UserApi.  # noqa: E501
        :type: str
        """

        self._principal = principal

    @property
    def created(self):
        """Gets the created of this UserApi.  # noqa: E501


        :return: The created of this UserApi.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this UserApi.


        :param created: The created of this UserApi.  # noqa: E501
        :type: datetime
        """

        self._created = created

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
        if issubclass(UserApi, dict):
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
        if not isinstance(other, UserApi):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserApi):
            return True

        return self.to_dict() != other.to_dict()
