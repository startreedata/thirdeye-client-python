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


class DimensionFilterContributionApiModel(object):
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
        'dimension_filters': 'dict(str, str)',
        'value': 'float',
        'percentage': 'float'
    }

    attribute_map = {
        'dimension_filters': 'dimensionFilters',
        'value': 'value',
        'percentage': 'percentage'
    }

    def __init__(self, dimension_filters=None, value=None, percentage=None, _configuration=None):  # noqa: E501
        """DimensionFilterContributionApiModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._dimension_filters = None
        self._value = None
        self._percentage = None
        self.discriminator = None

        if dimension_filters is not None:
            self.dimension_filters = dimension_filters
        if value is not None:
            self.value = value
        if percentage is not None:
            self.percentage = percentage

    @property
    def dimension_filters(self):
        """Gets the dimension_filters of this DimensionFilterContributionApiModel.  # noqa: E501


        :return: The dimension_filters of this DimensionFilterContributionApiModel.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._dimension_filters

    @dimension_filters.setter
    def dimension_filters(self, dimension_filters):
        """Sets the dimension_filters of this DimensionFilterContributionApiModel.


        :param dimension_filters: The dimension_filters of this DimensionFilterContributionApiModel.  # noqa: E501
        :type: dict(str, str)
        """

        self._dimension_filters = dimension_filters

    @property
    def value(self):
        """Gets the value of this DimensionFilterContributionApiModel.  # noqa: E501


        :return: The value of this DimensionFilterContributionApiModel.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this DimensionFilterContributionApiModel.


        :param value: The value of this DimensionFilterContributionApiModel.  # noqa: E501
        :type: float
        """

        self._value = value

    @property
    def percentage(self):
        """Gets the percentage of this DimensionFilterContributionApiModel.  # noqa: E501


        :return: The percentage of this DimensionFilterContributionApiModel.  # noqa: E501
        :rtype: float
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """Sets the percentage of this DimensionFilterContributionApiModel.


        :param percentage: The percentage of this DimensionFilterContributionApiModel.  # noqa: E501
        :type: float
        """

        self._percentage = percentage

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
        if issubclass(DimensionFilterContributionApiModel, dict):
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
        if not isinstance(other, DimensionFilterContributionApiModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DimensionFilterContributionApiModel):
            return True

        return self.to_dict() != other.to_dict()
