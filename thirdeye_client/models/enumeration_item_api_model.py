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


class EnumerationItemApiModel(object):
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
        'description': 'str',
        'params': 'dict(str, object)',
        'alerts': 'list[AlertApiModel]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'params': 'params',
        'alerts': 'alerts'
    }

    def __init__(self, id=None, name=None, description=None, params=None, alerts=None, _configuration=None):  # noqa: E501
        """EnumerationItemApiModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._description = None
        self._params = None
        self._alerts = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if params is not None:
            self.params = params
        if alerts is not None:
            self.alerts = alerts

    @property
    def id(self):
        """Gets the id of this EnumerationItemApiModel.  # noqa: E501


        :return: The id of this EnumerationItemApiModel.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EnumerationItemApiModel.


        :param id: The id of this EnumerationItemApiModel.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this EnumerationItemApiModel.  # noqa: E501


        :return: The name of this EnumerationItemApiModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EnumerationItemApiModel.


        :param name: The name of this EnumerationItemApiModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this EnumerationItemApiModel.  # noqa: E501


        :return: The description of this EnumerationItemApiModel.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EnumerationItemApiModel.


        :param description: The description of this EnumerationItemApiModel.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def params(self):
        """Gets the params of this EnumerationItemApiModel.  # noqa: E501


        :return: The params of this EnumerationItemApiModel.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this EnumerationItemApiModel.


        :param params: The params of this EnumerationItemApiModel.  # noqa: E501
        :type: dict(str, object)
        """

        self._params = params

    @property
    def alerts(self):
        """Gets the alerts of this EnumerationItemApiModel.  # noqa: E501


        :return: The alerts of this EnumerationItemApiModel.  # noqa: E501
        :rtype: list[AlertApiModel]
        """
        return self._alerts

    @alerts.setter
    def alerts(self, alerts):
        """Sets the alerts of this EnumerationItemApiModel.


        :param alerts: The alerts of this EnumerationItemApiModel.  # noqa: E501
        :type: list[AlertApiModel]
        """

        self._alerts = alerts

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
        if issubclass(EnumerationItemApiModel, dict):
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
        if not isinstance(other, EnumerationItemApiModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EnumerationItemApiModel):
            return True

        return self.to_dict() != other.to_dict()
