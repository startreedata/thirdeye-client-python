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


class RcaResource(object):
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
        'rca_investigation_resource': 'RcaInvestigationResource',
        'rca_metric_resource': 'RcaMetricResource',
        'rca_related_resource': 'RcaRelatedResource',
        'dimension_analysis_resource': 'RcaDimensionAnalysisResource'
    }

    attribute_map = {
        'rca_investigation_resource': 'rcaInvestigationResource',
        'rca_metric_resource': 'rcaMetricResource',
        'rca_related_resource': 'rcaRelatedResource',
        'dimension_analysis_resource': 'dimensionAnalysisResource'
    }

    def __init__(self, rca_investigation_resource=None, rca_metric_resource=None, rca_related_resource=None, dimension_analysis_resource=None, _configuration=None):  # noqa: E501
        """RcaResource - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._rca_investigation_resource = None
        self._rca_metric_resource = None
        self._rca_related_resource = None
        self._dimension_analysis_resource = None
        self.discriminator = None

        if rca_investigation_resource is not None:
            self.rca_investigation_resource = rca_investigation_resource
        if rca_metric_resource is not None:
            self.rca_metric_resource = rca_metric_resource
        if rca_related_resource is not None:
            self.rca_related_resource = rca_related_resource
        if dimension_analysis_resource is not None:
            self.dimension_analysis_resource = dimension_analysis_resource

    @property
    def rca_investigation_resource(self):
        """Gets the rca_investigation_resource of this RcaResource.  # noqa: E501


        :return: The rca_investigation_resource of this RcaResource.  # noqa: E501
        :rtype: RcaInvestigationResource
        """
        return self._rca_investigation_resource

    @rca_investigation_resource.setter
    def rca_investigation_resource(self, rca_investigation_resource):
        """Sets the rca_investigation_resource of this RcaResource.


        :param rca_investigation_resource: The rca_investigation_resource of this RcaResource.  # noqa: E501
        :type: RcaInvestigationResource
        """

        self._rca_investigation_resource = rca_investigation_resource

    @property
    def rca_metric_resource(self):
        """Gets the rca_metric_resource of this RcaResource.  # noqa: E501


        :return: The rca_metric_resource of this RcaResource.  # noqa: E501
        :rtype: RcaMetricResource
        """
        return self._rca_metric_resource

    @rca_metric_resource.setter
    def rca_metric_resource(self, rca_metric_resource):
        """Sets the rca_metric_resource of this RcaResource.


        :param rca_metric_resource: The rca_metric_resource of this RcaResource.  # noqa: E501
        :type: RcaMetricResource
        """

        self._rca_metric_resource = rca_metric_resource

    @property
    def rca_related_resource(self):
        """Gets the rca_related_resource of this RcaResource.  # noqa: E501


        :return: The rca_related_resource of this RcaResource.  # noqa: E501
        :rtype: RcaRelatedResource
        """
        return self._rca_related_resource

    @rca_related_resource.setter
    def rca_related_resource(self, rca_related_resource):
        """Sets the rca_related_resource of this RcaResource.


        :param rca_related_resource: The rca_related_resource of this RcaResource.  # noqa: E501
        :type: RcaRelatedResource
        """

        self._rca_related_resource = rca_related_resource

    @property
    def dimension_analysis_resource(self):
        """Gets the dimension_analysis_resource of this RcaResource.  # noqa: E501


        :return: The dimension_analysis_resource of this RcaResource.  # noqa: E501
        :rtype: RcaDimensionAnalysisResource
        """
        return self._dimension_analysis_resource

    @dimension_analysis_resource.setter
    def dimension_analysis_resource(self, dimension_analysis_resource):
        """Sets the dimension_analysis_resource of this RcaResource.


        :param dimension_analysis_resource: The dimension_analysis_resource of this RcaResource.  # noqa: E501
        :type: RcaDimensionAnalysisResource
        """

        self._dimension_analysis_resource = dimension_analysis_resource

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
        if issubclass(RcaResource, dict):
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
        if not isinstance(other, RcaResource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RcaResource):
            return True

        return self.to_dict() != other.to_dict()