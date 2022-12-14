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


class DataSourceApiModel(object):
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
        'name': 'str',
        'type': 'str',
        'properties': 'dict(str, object)',
        'meta_list': 'list[DataSourceMetaApiModel]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'properties': 'properties',
        'meta_list': 'metaList'
    }

    def __init__(self, id=None, name=None, type=None, properties=None, meta_list=None, _configuration=None):  # noqa: E501
        """DataSourceApiModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._type = None
        self._properties = None
        self._meta_list = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if properties is not None:
            self.properties = properties
        if meta_list is not None:
            self.meta_list = meta_list

    @property
    def id(self):
        """Gets the id of this DataSourceApiModel.  # noqa: E501


        :return: The id of this DataSourceApiModel.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DataSourceApiModel.


        :param id: The id of this DataSourceApiModel.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this DataSourceApiModel.  # noqa: E501


        :return: The name of this DataSourceApiModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DataSourceApiModel.


        :param name: The name of this DataSourceApiModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this DataSourceApiModel.  # noqa: E501


        :return: The type of this DataSourceApiModel.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DataSourceApiModel.


        :param type: The type of this DataSourceApiModel.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def properties(self):
        """Gets the properties of this DataSourceApiModel.  # noqa: E501


        :return: The properties of this DataSourceApiModel.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this DataSourceApiModel.


        :param properties: The properties of this DataSourceApiModel.  # noqa: E501
        :type: dict(str, object)
        """

        self._properties = properties

    @property
    def meta_list(self):
        """Gets the meta_list of this DataSourceApiModel.  # noqa: E501


        :return: The meta_list of this DataSourceApiModel.  # noqa: E501
        :rtype: list[DataSourceMetaApiModel]
        """
        return self._meta_list

    @meta_list.setter
    def meta_list(self, meta_list):
        """Sets the meta_list of this DataSourceApiModel.


        :param meta_list: The meta_list of this DataSourceApiModel.  # noqa: E501
        :type: list[DataSourceMetaApiModel]
        """

        self._meta_list = meta_list

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
        if issubclass(DataSourceApiModel, dict):
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
        if not isinstance(other, DataSourceApiModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DataSourceApiModel):
            return True

        return self.to_dict() != other.to_dict()
