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


class ApiResourceModel(object):
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
        'auth_resource': 'AuthResourceModel',
        'auth_info_resource': 'AuthInfoResourceModel',
        'data_source_resource': 'DataSourceResourceModel',
        'dataset_resource': 'DatasetResourceModel',
        'metric_resource': 'MetricResourceModel',
        'alert_resource': 'AlertResourceModel',
        'alert_template_resource': 'AlertTemplateResourceModel',
        'subscription_group_resource': 'SubscriptionGroupResourceModel',
        'anomaly_resource': 'AnomalyResourceModel',
        'entity_resource': 'EntityResourceModel',
        'rca_resource': 'RcaResourceModel',
        'event_resource': 'EventResourceModel',
        'task_resource': 'TaskResourceModel',
        'enumeration_item_resource': 'EnumerationItemResourceModel',
        'analytics_resource': 'AppAnalyticsResourceModel',
        'uiresource': 'UiResourceModel'
    }

    attribute_map = {
        'auth_resource': 'authResource',
        'auth_info_resource': 'authInfoResource',
        'data_source_resource': 'dataSourceResource',
        'dataset_resource': 'datasetResource',
        'metric_resource': 'metricResource',
        'alert_resource': 'alertResource',
        'alert_template_resource': 'alertTemplateResource',
        'subscription_group_resource': 'subscriptionGroupResource',
        'anomaly_resource': 'anomalyResource',
        'entity_resource': 'entityResource',
        'rca_resource': 'rcaResource',
        'event_resource': 'eventResource',
        'task_resource': 'taskResource',
        'enumeration_item_resource': 'enumerationItemResource',
        'analytics_resource': 'analyticsResource',
        'uiresource': 'uiresource'
    }

    def __init__(self, auth_resource=None, auth_info_resource=None, data_source_resource=None, dataset_resource=None, metric_resource=None, alert_resource=None, alert_template_resource=None, subscription_group_resource=None, anomaly_resource=None, entity_resource=None, rca_resource=None, event_resource=None, task_resource=None, enumeration_item_resource=None, analytics_resource=None, uiresource=None, _configuration=None):  # noqa: E501
        """ApiResourceModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._auth_resource = None
        self._auth_info_resource = None
        self._data_source_resource = None
        self._dataset_resource = None
        self._metric_resource = None
        self._alert_resource = None
        self._alert_template_resource = None
        self._subscription_group_resource = None
        self._anomaly_resource = None
        self._entity_resource = None
        self._rca_resource = None
        self._event_resource = None
        self._task_resource = None
        self._enumeration_item_resource = None
        self._analytics_resource = None
        self._uiresource = None
        self.discriminator = None

        if auth_resource is not None:
            self.auth_resource = auth_resource
        if auth_info_resource is not None:
            self.auth_info_resource = auth_info_resource
        if data_source_resource is not None:
            self.data_source_resource = data_source_resource
        if dataset_resource is not None:
            self.dataset_resource = dataset_resource
        if metric_resource is not None:
            self.metric_resource = metric_resource
        if alert_resource is not None:
            self.alert_resource = alert_resource
        if alert_template_resource is not None:
            self.alert_template_resource = alert_template_resource
        if subscription_group_resource is not None:
            self.subscription_group_resource = subscription_group_resource
        if anomaly_resource is not None:
            self.anomaly_resource = anomaly_resource
        if entity_resource is not None:
            self.entity_resource = entity_resource
        if rca_resource is not None:
            self.rca_resource = rca_resource
        if event_resource is not None:
            self.event_resource = event_resource
        if task_resource is not None:
            self.task_resource = task_resource
        if enumeration_item_resource is not None:
            self.enumeration_item_resource = enumeration_item_resource
        if analytics_resource is not None:
            self.analytics_resource = analytics_resource
        if uiresource is not None:
            self.uiresource = uiresource

    @property
    def auth_resource(self):
        """Gets the auth_resource of this ApiResourceModel.  # noqa: E501


        :return: The auth_resource of this ApiResourceModel.  # noqa: E501
        :rtype: AuthResourceModel
        """
        return self._auth_resource

    @auth_resource.setter
    def auth_resource(self, auth_resource):
        """Sets the auth_resource of this ApiResourceModel.


        :param auth_resource: The auth_resource of this ApiResourceModel.  # noqa: E501
        :type: AuthResourceModel
        """

        self._auth_resource = auth_resource

    @property
    def auth_info_resource(self):
        """Gets the auth_info_resource of this ApiResourceModel.  # noqa: E501


        :return: The auth_info_resource of this ApiResourceModel.  # noqa: E501
        :rtype: AuthInfoResourceModel
        """
        return self._auth_info_resource

    @auth_info_resource.setter
    def auth_info_resource(self, auth_info_resource):
        """Sets the auth_info_resource of this ApiResourceModel.


        :param auth_info_resource: The auth_info_resource of this ApiResourceModel.  # noqa: E501
        :type: AuthInfoResourceModel
        """

        self._auth_info_resource = auth_info_resource

    @property
    def data_source_resource(self):
        """Gets the data_source_resource of this ApiResourceModel.  # noqa: E501


        :return: The data_source_resource of this ApiResourceModel.  # noqa: E501
        :rtype: DataSourceResourceModel
        """
        return self._data_source_resource

    @data_source_resource.setter
    def data_source_resource(self, data_source_resource):
        """Sets the data_source_resource of this ApiResourceModel.


        :param data_source_resource: The data_source_resource of this ApiResourceModel.  # noqa: E501
        :type: DataSourceResourceModel
        """

        self._data_source_resource = data_source_resource

    @property
    def dataset_resource(self):
        """Gets the dataset_resource of this ApiResourceModel.  # noqa: E501


        :return: The dataset_resource of this ApiResourceModel.  # noqa: E501
        :rtype: DatasetResourceModel
        """
        return self._dataset_resource

    @dataset_resource.setter
    def dataset_resource(self, dataset_resource):
        """Sets the dataset_resource of this ApiResourceModel.


        :param dataset_resource: The dataset_resource of this ApiResourceModel.  # noqa: E501
        :type: DatasetResourceModel
        """

        self._dataset_resource = dataset_resource

    @property
    def metric_resource(self):
        """Gets the metric_resource of this ApiResourceModel.  # noqa: E501


        :return: The metric_resource of this ApiResourceModel.  # noqa: E501
        :rtype: MetricResourceModel
        """
        return self._metric_resource

    @metric_resource.setter
    def metric_resource(self, metric_resource):
        """Sets the metric_resource of this ApiResourceModel.


        :param metric_resource: The metric_resource of this ApiResourceModel.  # noqa: E501
        :type: MetricResourceModel
        """

        self._metric_resource = metric_resource

    @property
    def alert_resource(self):
        """Gets the alert_resource of this ApiResourceModel.  # noqa: E501


        :return: The alert_resource of this ApiResourceModel.  # noqa: E501
        :rtype: AlertResourceModel
        """
        return self._alert_resource

    @alert_resource.setter
    def alert_resource(self, alert_resource):
        """Sets the alert_resource of this ApiResourceModel.


        :param alert_resource: The alert_resource of this ApiResourceModel.  # noqa: E501
        :type: AlertResourceModel
        """

        self._alert_resource = alert_resource

    @property
    def alert_template_resource(self):
        """Gets the alert_template_resource of this ApiResourceModel.  # noqa: E501


        :return: The alert_template_resource of this ApiResourceModel.  # noqa: E501
        :rtype: AlertTemplateResourceModel
        """
        return self._alert_template_resource

    @alert_template_resource.setter
    def alert_template_resource(self, alert_template_resource):
        """Sets the alert_template_resource of this ApiResourceModel.


        :param alert_template_resource: The alert_template_resource of this ApiResourceModel.  # noqa: E501
        :type: AlertTemplateResourceModel
        """

        self._alert_template_resource = alert_template_resource

    @property
    def subscription_group_resource(self):
        """Gets the subscription_group_resource of this ApiResourceModel.  # noqa: E501


        :return: The subscription_group_resource of this ApiResourceModel.  # noqa: E501
        :rtype: SubscriptionGroupResourceModel
        """
        return self._subscription_group_resource

    @subscription_group_resource.setter
    def subscription_group_resource(self, subscription_group_resource):
        """Sets the subscription_group_resource of this ApiResourceModel.


        :param subscription_group_resource: The subscription_group_resource of this ApiResourceModel.  # noqa: E501
        :type: SubscriptionGroupResourceModel
        """

        self._subscription_group_resource = subscription_group_resource

    @property
    def anomaly_resource(self):
        """Gets the anomaly_resource of this ApiResourceModel.  # noqa: E501


        :return: The anomaly_resource of this ApiResourceModel.  # noqa: E501
        :rtype: AnomalyResourceModel
        """
        return self._anomaly_resource

    @anomaly_resource.setter
    def anomaly_resource(self, anomaly_resource):
        """Sets the anomaly_resource of this ApiResourceModel.


        :param anomaly_resource: The anomaly_resource of this ApiResourceModel.  # noqa: E501
        :type: AnomalyResourceModel
        """

        self._anomaly_resource = anomaly_resource

    @property
    def entity_resource(self):
        """Gets the entity_resource of this ApiResourceModel.  # noqa: E501


        :return: The entity_resource of this ApiResourceModel.  # noqa: E501
        :rtype: EntityResourceModel
        """
        return self._entity_resource

    @entity_resource.setter
    def entity_resource(self, entity_resource):
        """Sets the entity_resource of this ApiResourceModel.


        :param entity_resource: The entity_resource of this ApiResourceModel.  # noqa: E501
        :type: EntityResourceModel
        """

        self._entity_resource = entity_resource

    @property
    def rca_resource(self):
        """Gets the rca_resource of this ApiResourceModel.  # noqa: E501


        :return: The rca_resource of this ApiResourceModel.  # noqa: E501
        :rtype: RcaResourceModel
        """
        return self._rca_resource

    @rca_resource.setter
    def rca_resource(self, rca_resource):
        """Sets the rca_resource of this ApiResourceModel.


        :param rca_resource: The rca_resource of this ApiResourceModel.  # noqa: E501
        :type: RcaResourceModel
        """

        self._rca_resource = rca_resource

    @property
    def event_resource(self):
        """Gets the event_resource of this ApiResourceModel.  # noqa: E501


        :return: The event_resource of this ApiResourceModel.  # noqa: E501
        :rtype: EventResourceModel
        """
        return self._event_resource

    @event_resource.setter
    def event_resource(self, event_resource):
        """Sets the event_resource of this ApiResourceModel.


        :param event_resource: The event_resource of this ApiResourceModel.  # noqa: E501
        :type: EventResourceModel
        """

        self._event_resource = event_resource

    @property
    def task_resource(self):
        """Gets the task_resource of this ApiResourceModel.  # noqa: E501


        :return: The task_resource of this ApiResourceModel.  # noqa: E501
        :rtype: TaskResourceModel
        """
        return self._task_resource

    @task_resource.setter
    def task_resource(self, task_resource):
        """Sets the task_resource of this ApiResourceModel.


        :param task_resource: The task_resource of this ApiResourceModel.  # noqa: E501
        :type: TaskResourceModel
        """

        self._task_resource = task_resource

    @property
    def enumeration_item_resource(self):
        """Gets the enumeration_item_resource of this ApiResourceModel.  # noqa: E501


        :return: The enumeration_item_resource of this ApiResourceModel.  # noqa: E501
        :rtype: EnumerationItemResourceModel
        """
        return self._enumeration_item_resource

    @enumeration_item_resource.setter
    def enumeration_item_resource(self, enumeration_item_resource):
        """Sets the enumeration_item_resource of this ApiResourceModel.


        :param enumeration_item_resource: The enumeration_item_resource of this ApiResourceModel.  # noqa: E501
        :type: EnumerationItemResourceModel
        """

        self._enumeration_item_resource = enumeration_item_resource

    @property
    def analytics_resource(self):
        """Gets the analytics_resource of this ApiResourceModel.  # noqa: E501


        :return: The analytics_resource of this ApiResourceModel.  # noqa: E501
        :rtype: AppAnalyticsResourceModel
        """
        return self._analytics_resource

    @analytics_resource.setter
    def analytics_resource(self, analytics_resource):
        """Sets the analytics_resource of this ApiResourceModel.


        :param analytics_resource: The analytics_resource of this ApiResourceModel.  # noqa: E501
        :type: AppAnalyticsResourceModel
        """

        self._analytics_resource = analytics_resource

    @property
    def uiresource(self):
        """Gets the uiresource of this ApiResourceModel.  # noqa: E501


        :return: The uiresource of this ApiResourceModel.  # noqa: E501
        :rtype: UiResourceModel
        """
        return self._uiresource

    @uiresource.setter
    def uiresource(self, uiresource):
        """Sets the uiresource of this ApiResourceModel.


        :param uiresource: The uiresource of this ApiResourceModel.  # noqa: E501
        :type: UiResourceModel
        """

        self._uiresource = uiresource

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
        if issubclass(ApiResourceModel, dict):
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
        if not isinstance(other, ApiResourceModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApiResourceModel):
            return True

        return self.to_dict() != other.to_dict()
