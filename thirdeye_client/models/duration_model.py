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


class DurationModel(object):
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
        'seconds': 'int',
        'negative': 'bool',
        'units': 'list[TemporalUnitModel]',
        'zero': 'bool',
        'nano': 'int'
    }

    attribute_map = {
        'seconds': 'seconds',
        'negative': 'negative',
        'units': 'units',
        'zero': 'zero',
        'nano': 'nano'
    }

    def __init__(self, seconds=None, negative=None, units=None, zero=None, nano=None, _configuration=None):  # noqa: E501
        """DurationModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._seconds = None
        self._negative = None
        self._units = None
        self._zero = None
        self._nano = None
        self.discriminator = None

        if seconds is not None:
            self.seconds = seconds
        if negative is not None:
            self.negative = negative
        if units is not None:
            self.units = units
        if zero is not None:
            self.zero = zero
        if nano is not None:
            self.nano = nano

    @property
    def seconds(self):
        """Gets the seconds of this DurationModel.  # noqa: E501


        :return: The seconds of this DurationModel.  # noqa: E501
        :rtype: int
        """
        return self._seconds

    @seconds.setter
    def seconds(self, seconds):
        """Sets the seconds of this DurationModel.


        :param seconds: The seconds of this DurationModel.  # noqa: E501
        :type: int
        """

        self._seconds = seconds

    @property
    def negative(self):
        """Gets the negative of this DurationModel.  # noqa: E501


        :return: The negative of this DurationModel.  # noqa: E501
        :rtype: bool
        """
        return self._negative

    @negative.setter
    def negative(self, negative):
        """Sets the negative of this DurationModel.


        :param negative: The negative of this DurationModel.  # noqa: E501
        :type: bool
        """

        self._negative = negative

    @property
    def units(self):
        """Gets the units of this DurationModel.  # noqa: E501


        :return: The units of this DurationModel.  # noqa: E501
        :rtype: list[TemporalUnitModel]
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this DurationModel.


        :param units: The units of this DurationModel.  # noqa: E501
        :type: list[TemporalUnitModel]
        """

        self._units = units

    @property
    def zero(self):
        """Gets the zero of this DurationModel.  # noqa: E501


        :return: The zero of this DurationModel.  # noqa: E501
        :rtype: bool
        """
        return self._zero

    @zero.setter
    def zero(self, zero):
        """Sets the zero of this DurationModel.


        :param zero: The zero of this DurationModel.  # noqa: E501
        :type: bool
        """

        self._zero = zero

    @property
    def nano(self):
        """Gets the nano of this DurationModel.  # noqa: E501


        :return: The nano of this DurationModel.  # noqa: E501
        :rtype: int
        """
        return self._nano

    @nano.setter
    def nano(self, nano):
        """Sets the nano of this DurationModel.


        :param nano: The nano of this DurationModel.  # noqa: E501
        :type: int
        """

        self._nano = nano

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
        if issubclass(DurationModel, dict):
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
        if not isinstance(other, DurationModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DurationModel):
            return True

        return self.to_dict() != other.to_dict()
