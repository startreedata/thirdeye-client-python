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


class AnomalyFeedbackApi(object):
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
        'owner': 'UserApi',
        'type': 'str',
        'comment': 'str'
    }

    attribute_map = {
        'id': 'id',
        'owner': 'owner',
        'type': 'type',
        'comment': 'comment'
    }

    def __init__(self, id=None, owner=None, type=None, comment=None, _configuration=None):  # noqa: E501
        """AnomalyFeedbackApi - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._owner = None
        self._type = None
        self._comment = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if owner is not None:
            self.owner = owner
        if type is not None:
            self.type = type
        if comment is not None:
            self.comment = comment

    @property
    def id(self):
        """Gets the id of this AnomalyFeedbackApi.  # noqa: E501


        :return: The id of this AnomalyFeedbackApi.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AnomalyFeedbackApi.


        :param id: The id of this AnomalyFeedbackApi.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def owner(self):
        """Gets the owner of this AnomalyFeedbackApi.  # noqa: E501


        :return: The owner of this AnomalyFeedbackApi.  # noqa: E501
        :rtype: UserApi
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this AnomalyFeedbackApi.


        :param owner: The owner of this AnomalyFeedbackApi.  # noqa: E501
        :type: UserApi
        """

        self._owner = owner

    @property
    def type(self):
        """Gets the type of this AnomalyFeedbackApi.  # noqa: E501


        :return: The type of this AnomalyFeedbackApi.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AnomalyFeedbackApi.


        :param type: The type of this AnomalyFeedbackApi.  # noqa: E501
        :type: str
        """
        allowed_values = ["ANOMALY", "ANOMALY_EXPECTED", "NOT_ANOMALY", "ANOMALY_NEW_TREND", "NO_FEEDBACK"]  # noqa: E501
        if (self._configuration.client_side_validation and
                type not in allowed_values):
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def comment(self):
        """Gets the comment of this AnomalyFeedbackApi.  # noqa: E501


        :return: The comment of this AnomalyFeedbackApi.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this AnomalyFeedbackApi.


        :param comment: The comment of this AnomalyFeedbackApi.  # noqa: E501
        :type: str
        """

        self._comment = comment

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
        if issubclass(AnomalyFeedbackApi, dict):
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
        if not isinstance(other, AnomalyFeedbackApi):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AnomalyFeedbackApi):
            return True

        return self.to_dict() != other.to_dict()
