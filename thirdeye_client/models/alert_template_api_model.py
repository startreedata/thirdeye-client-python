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


class AlertTemplateApiModel(object):
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
        'cron': 'str',
        'created': 'datetime',
        'updated': 'datetime',
        'owner': 'UserApiModel',
        'nodes': 'list[PlanNodeApiModel]',
        'rca': 'RcaMetadataApiModel',
        'metadata': 'AlertMetadataApiModel',
        'default_properties': 'dict(str, object)',
        'properties': 'list[TemplatePropertyMetadataModel]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'cron': 'cron',
        'created': 'created',
        'updated': 'updated',
        'owner': 'owner',
        'nodes': 'nodes',
        'rca': 'rca',
        'metadata': 'metadata',
        'default_properties': 'defaultProperties',
        'properties': 'properties'
    }

    def __init__(self, id=None, name=None, description=None, cron=None, created=None, updated=None, owner=None, nodes=None, rca=None, metadata=None, default_properties=None, properties=None, _configuration=None):  # noqa: E501
        """AlertTemplateApiModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._description = None
        self._cron = None
        self._created = None
        self._updated = None
        self._owner = None
        self._nodes = None
        self._rca = None
        self._metadata = None
        self._default_properties = None
        self._properties = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if cron is not None:
            self.cron = cron
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated
        if owner is not None:
            self.owner = owner
        if nodes is not None:
            self.nodes = nodes
        if rca is not None:
            self.rca = rca
        if metadata is not None:
            self.metadata = metadata
        if default_properties is not None:
            self.default_properties = default_properties
        if properties is not None:
            self.properties = properties

    @property
    def id(self):
        """Gets the id of this AlertTemplateApiModel.  # noqa: E501


        :return: The id of this AlertTemplateApiModel.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AlertTemplateApiModel.


        :param id: The id of this AlertTemplateApiModel.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this AlertTemplateApiModel.  # noqa: E501


        :return: The name of this AlertTemplateApiModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AlertTemplateApiModel.


        :param name: The name of this AlertTemplateApiModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this AlertTemplateApiModel.  # noqa: E501


        :return: The description of this AlertTemplateApiModel.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AlertTemplateApiModel.


        :param description: The description of this AlertTemplateApiModel.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def cron(self):
        """Gets the cron of this AlertTemplateApiModel.  # noqa: E501


        :return: The cron of this AlertTemplateApiModel.  # noqa: E501
        :rtype: str
        """
        return self._cron

    @cron.setter
    def cron(self, cron):
        """Sets the cron of this AlertTemplateApiModel.


        :param cron: The cron of this AlertTemplateApiModel.  # noqa: E501
        :type: str
        """

        self._cron = cron

    @property
    def created(self):
        """Gets the created of this AlertTemplateApiModel.  # noqa: E501


        :return: The created of this AlertTemplateApiModel.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this AlertTemplateApiModel.


        :param created: The created of this AlertTemplateApiModel.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def updated(self):
        """Gets the updated of this AlertTemplateApiModel.  # noqa: E501


        :return: The updated of this AlertTemplateApiModel.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this AlertTemplateApiModel.


        :param updated: The updated of this AlertTemplateApiModel.  # noqa: E501
        :type: datetime
        """

        self._updated = updated

    @property
    def owner(self):
        """Gets the owner of this AlertTemplateApiModel.  # noqa: E501


        :return: The owner of this AlertTemplateApiModel.  # noqa: E501
        :rtype: UserApiModel
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this AlertTemplateApiModel.


        :param owner: The owner of this AlertTemplateApiModel.  # noqa: E501
        :type: UserApiModel
        """

        self._owner = owner

    @property
    def nodes(self):
        """Gets the nodes of this AlertTemplateApiModel.  # noqa: E501


        :return: The nodes of this AlertTemplateApiModel.  # noqa: E501
        :rtype: list[PlanNodeApiModel]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this AlertTemplateApiModel.


        :param nodes: The nodes of this AlertTemplateApiModel.  # noqa: E501
        :type: list[PlanNodeApiModel]
        """

        self._nodes = nodes

    @property
    def rca(self):
        """Gets the rca of this AlertTemplateApiModel.  # noqa: E501


        :return: The rca of this AlertTemplateApiModel.  # noqa: E501
        :rtype: RcaMetadataApiModel
        """
        return self._rca

    @rca.setter
    def rca(self, rca):
        """Sets the rca of this AlertTemplateApiModel.


        :param rca: The rca of this AlertTemplateApiModel.  # noqa: E501
        :type: RcaMetadataApiModel
        """

        self._rca = rca

    @property
    def metadata(self):
        """Gets the metadata of this AlertTemplateApiModel.  # noqa: E501


        :return: The metadata of this AlertTemplateApiModel.  # noqa: E501
        :rtype: AlertMetadataApiModel
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this AlertTemplateApiModel.


        :param metadata: The metadata of this AlertTemplateApiModel.  # noqa: E501
        :type: AlertMetadataApiModel
        """

        self._metadata = metadata

    @property
    def default_properties(self):
        """Gets the default_properties of this AlertTemplateApiModel.  # noqa: E501


        :return: The default_properties of this AlertTemplateApiModel.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._default_properties

    @default_properties.setter
    def default_properties(self, default_properties):
        """Sets the default_properties of this AlertTemplateApiModel.


        :param default_properties: The default_properties of this AlertTemplateApiModel.  # noqa: E501
        :type: dict(str, object)
        """

        self._default_properties = default_properties

    @property
    def properties(self):
        """Gets the properties of this AlertTemplateApiModel.  # noqa: E501


        :return: The properties of this AlertTemplateApiModel.  # noqa: E501
        :rtype: list[TemplatePropertyMetadataModel]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this AlertTemplateApiModel.


        :param properties: The properties of this AlertTemplateApiModel.  # noqa: E501
        :type: list[TemplatePropertyMetadataModel]
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
        if issubclass(AlertTemplateApiModel, dict):
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
        if not isinstance(other, AlertTemplateApiModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AlertTemplateApiModel):
            return True

        return self.to_dict() != other.to_dict()
