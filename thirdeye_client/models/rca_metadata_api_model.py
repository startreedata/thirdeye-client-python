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


class RcaMetadataApiModel(object):
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
        'datasource': 'str',
        'dataset': 'str',
        'metric': 'str',
        'aggregation_function': 'str',
        'granularity': 'str',
        'properties': 'dict(str, object)'
    }

    attribute_map = {
        'datasource': 'datasource',
        'dataset': 'dataset',
        'metric': 'metric',
        'aggregation_function': 'aggregationFunction',
        'granularity': 'granularity',
        'properties': 'properties'
    }

    def __init__(self, datasource=None, dataset=None, metric=None, aggregation_function=None, granularity=None, properties=None, _configuration=None):  # noqa: E501
        """RcaMetadataApiModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._datasource = None
        self._dataset = None
        self._metric = None
        self._aggregation_function = None
        self._granularity = None
        self._properties = None
        self.discriminator = None

        if datasource is not None:
            self.datasource = datasource
        if dataset is not None:
            self.dataset = dataset
        if metric is not None:
            self.metric = metric
        if aggregation_function is not None:
            self.aggregation_function = aggregation_function
        if granularity is not None:
            self.granularity = granularity
        if properties is not None:
            self.properties = properties

    @property
    def datasource(self):
        """Gets the datasource of this RcaMetadataApiModel.  # noqa: E501


        :return: The datasource of this RcaMetadataApiModel.  # noqa: E501
        :rtype: str
        """
        return self._datasource

    @datasource.setter
    def datasource(self, datasource):
        """Sets the datasource of this RcaMetadataApiModel.


        :param datasource: The datasource of this RcaMetadataApiModel.  # noqa: E501
        :type: str
        """

        self._datasource = datasource

    @property
    def dataset(self):
        """Gets the dataset of this RcaMetadataApiModel.  # noqa: E501


        :return: The dataset of this RcaMetadataApiModel.  # noqa: E501
        :rtype: str
        """
        return self._dataset

    @dataset.setter
    def dataset(self, dataset):
        """Sets the dataset of this RcaMetadataApiModel.


        :param dataset: The dataset of this RcaMetadataApiModel.  # noqa: E501
        :type: str
        """

        self._dataset = dataset

    @property
    def metric(self):
        """Gets the metric of this RcaMetadataApiModel.  # noqa: E501


        :return: The metric of this RcaMetadataApiModel.  # noqa: E501
        :rtype: str
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this RcaMetadataApiModel.


        :param metric: The metric of this RcaMetadataApiModel.  # noqa: E501
        :type: str
        """

        self._metric = metric

    @property
    def aggregation_function(self):
        """Gets the aggregation_function of this RcaMetadataApiModel.  # noqa: E501


        :return: The aggregation_function of this RcaMetadataApiModel.  # noqa: E501
        :rtype: str
        """
        return self._aggregation_function

    @aggregation_function.setter
    def aggregation_function(self, aggregation_function):
        """Sets the aggregation_function of this RcaMetadataApiModel.


        :param aggregation_function: The aggregation_function of this RcaMetadataApiModel.  # noqa: E501
        :type: str
        """

        self._aggregation_function = aggregation_function

    @property
    def granularity(self):
        """Gets the granularity of this RcaMetadataApiModel.  # noqa: E501


        :return: The granularity of this RcaMetadataApiModel.  # noqa: E501
        :rtype: str
        """
        return self._granularity

    @granularity.setter
    def granularity(self, granularity):
        """Sets the granularity of this RcaMetadataApiModel.


        :param granularity: The granularity of this RcaMetadataApiModel.  # noqa: E501
        :type: str
        """

        self._granularity = granularity

    @property
    def properties(self):
        """Gets the properties of this RcaMetadataApiModel.  # noqa: E501


        :return: The properties of this RcaMetadataApiModel.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this RcaMetadataApiModel.


        :param properties: The properties of this RcaMetadataApiModel.  # noqa: E501
        :type: dict(str, object)
        """

        self._properties = properties

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
        if issubclass(RcaMetadataApiModel, dict):
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
        if not isinstance(other, RcaMetadataApiModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RcaMetadataApiModel):
            return True

        return self.to_dict() != other.to_dict()
