# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import thirdeye_client
from thirdeye_client.api.app_analytics_api import AppAnalyticsApi  # noqa: E501
from thirdeye_client.rest import ApiException


class TestAppAnalyticsApi(unittest.TestCase):
    """AppAnalyticsApi unit test stubs"""

    def setUp(self):
        self.api = thirdeye_client.api.app_analytics_api.AppAnalyticsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_analytics_payload(self):
        """Test case for get_analytics_payload

        """
        pass

    def test_get_version(self):
        """Test case for get_version

        """
        pass


if __name__ == '__main__':
    unittest.main()
