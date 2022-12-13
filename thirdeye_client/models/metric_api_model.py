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


class MetricApiModel(object):
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
        'urn': 'str',
        'dataset': 'DatasetApiModel',
        'active': 'bool',
        'created': 'datetime',
        'updated': 'datetime',
        'derived_metric_expression': 'str',
        'aggregation_column': 'str',
        'datatype': 'str',
        'aggregation_function': 'str',
        'views': 'list[LogicalViewModel]',
        'where': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'urn': 'urn',
        'dataset': 'dataset',
        'active': 'active',
        'created': 'created',
        'updated': 'updated',
        'derived_metric_expression': 'derivedMetricExpression',
        'aggregation_column': 'aggregationColumn',
        'datatype': 'datatype',
        'aggregation_function': 'aggregationFunction',
        'views': 'views',
        'where': 'where'
    }

    def __init__(self, id=None, name=None, urn=None, dataset=None, active=None, created=None, updated=None, derived_metric_expression=None, aggregation_column=None, datatype=None, aggregation_function=None, views=None, where=None, _configuration=None):  # noqa: E501
        """MetricApiModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._urn = None
        self._dataset = None
        self._active = None
        self._created = None
        self._updated = None
        self._derived_metric_expression = None
        self._aggregation_column = None
        self._datatype = None
        self._aggregation_function = None
        self._views = None
        self._where = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if urn is not None:
            self.urn = urn
        if dataset is not None:
            self.dataset = dataset
        if active is not None:
            self.active = active
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated
        if derived_metric_expression is not None:
            self.derived_metric_expression = derived_metric_expression
        if aggregation_column is not None:
            self.aggregation_column = aggregation_column
        if datatype is not None:
            self.datatype = datatype
        if aggregation_function is not None:
            self.aggregation_function = aggregation_function
        if views is not None:
            self.views = views
        if where is not None:
            self.where = where

    @property
    def id(self):
        """Gets the id of this MetricApiModel.  # noqa: E501


        :return: The id of this MetricApiModel.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MetricApiModel.


        :param id: The id of this MetricApiModel.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this MetricApiModel.  # noqa: E501


        :return: The name of this MetricApiModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MetricApiModel.


        :param name: The name of this MetricApiModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def urn(self):
        """Gets the urn of this MetricApiModel.  # noqa: E501


        :return: The urn of this MetricApiModel.  # noqa: E501
        :rtype: str
        """
        return self._urn

    @urn.setter
    def urn(self, urn):
        """Sets the urn of this MetricApiModel.


        :param urn: The urn of this MetricApiModel.  # noqa: E501
        :type: str
        """

        self._urn = urn

    @property
    def dataset(self):
        """Gets the dataset of this MetricApiModel.  # noqa: E501


        :return: The dataset of this MetricApiModel.  # noqa: E501
        :rtype: DatasetApiModel
        """
        return self._dataset

    @dataset.setter
    def dataset(self, dataset):
        """Sets the dataset of this MetricApiModel.


        :param dataset: The dataset of this MetricApiModel.  # noqa: E501
        :type: DatasetApiModel
        """

        self._dataset = dataset

    @property
    def active(self):
        """Gets the active of this MetricApiModel.  # noqa: E501


        :return: The active of this MetricApiModel.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this MetricApiModel.


        :param active: The active of this MetricApiModel.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def created(self):
        """Gets the created of this MetricApiModel.  # noqa: E501


        :return: The created of this MetricApiModel.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this MetricApiModel.


        :param created: The created of this MetricApiModel.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def updated(self):
        """Gets the updated of this MetricApiModel.  # noqa: E501


        :return: The updated of this MetricApiModel.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this MetricApiModel.


        :param updated: The updated of this MetricApiModel.  # noqa: E501
        :type: datetime
        """

        self._updated = updated

    @property
    def derived_metric_expression(self):
        """Gets the derived_metric_expression of this MetricApiModel.  # noqa: E501


        :return: The derived_metric_expression of this MetricApiModel.  # noqa: E501
        :rtype: str
        """
        return self._derived_metric_expression

    @derived_metric_expression.setter
    def derived_metric_expression(self, derived_metric_expression):
        """Sets the derived_metric_expression of this MetricApiModel.


        :param derived_metric_expression: The derived_metric_expression of this MetricApiModel.  # noqa: E501
        :type: str
        """

        self._derived_metric_expression = derived_metric_expression

    @property
    def aggregation_column(self):
        """Gets the aggregation_column of this MetricApiModel.  # noqa: E501


        :return: The aggregation_column of this MetricApiModel.  # noqa: E501
        :rtype: str
        """
        return self._aggregation_column

    @aggregation_column.setter
    def aggregation_column(self, aggregation_column):
        """Sets the aggregation_column of this MetricApiModel.


        :param aggregation_column: The aggregation_column of this MetricApiModel.  # noqa: E501
        :type: str
        """

        self._aggregation_column = aggregation_column

    @property
    def datatype(self):
        """Gets the datatype of this MetricApiModel.  # noqa: E501


        :return: The datatype of this MetricApiModel.  # noqa: E501
        :rtype: str
        """
        return self._datatype

    @datatype.setter
    def datatype(self, datatype):
        """Sets the datatype of this MetricApiModel.


        :param datatype: The datatype of this MetricApiModel.  # noqa: E501
        :type: str
        """
        allowed_values = ["INT", "SHORT", "LONG", "FLOAT", "DOUBLE"]  # noqa: E501
        if (self._configuration.client_side_validation and
                datatype not in allowed_values):
            raise ValueError(
                "Invalid value for `datatype` ({0}), must be one of {1}"  # noqa: E501
                .format(datatype, allowed_values)
            )

        self._datatype = datatype

    @property
    def aggregation_function(self):
        """Gets the aggregation_function of this MetricApiModel.  # noqa: E501


        :return: The aggregation_function of this MetricApiModel.  # noqa: E501
        :rtype: str
        """
        return self._aggregation_function

    @aggregation_function.setter
    def aggregation_function(self, aggregation_function):
        """Sets the aggregation_function of this MetricApiModel.


        :param aggregation_function: The aggregation_function of this MetricApiModel.  # noqa: E501
        :type: str
        """

        self._aggregation_function = aggregation_function

    @property
    def views(self):
        """Gets the views of this MetricApiModel.  # noqa: E501


        :return: The views of this MetricApiModel.  # noqa: E501
        :rtype: list[LogicalViewModel]
        """
        return self._views

    @views.setter
    def views(self, views):
        """Sets the views of this MetricApiModel.


        :param views: The views of this MetricApiModel.  # noqa: E501
        :type: list[LogicalViewModel]
        """

        self._views = views

    @property
    def where(self):
        """Gets the where of this MetricApiModel.  # noqa: E501


        :return: The where of this MetricApiModel.  # noqa: E501
        :rtype: str
        """
        return self._where

    @where.setter
    def where(self, where):
        """Sets the where of this MetricApiModel.


        :param where: The where of this MetricApiModel.  # noqa: E501
        :type: str
        """

        self._where = where

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
        if issubclass(MetricApiModel, dict):
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
        if not isinstance(other, MetricApiModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MetricApiModel):
            return True

        return self.to_dict() != other.to_dict()
