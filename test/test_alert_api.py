# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import thirdeye_client
from thirdeye_client.api.alert_api import AlertApi  # noqa: E501
from thirdeye_client.rest import ApiException


class TestAlertApi(unittest.TestCase):
    """AlertApi unit test stubs"""

    def setUp(self):
        self.api = thirdeye_client.api.alert_api.AlertApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_count_with_predicate3(self):
        """Test case for count_with_predicate3

        """
        pass

    def test_create_multiple3(self):
        """Test case for create_multiple3

        """
        pass

    def test_delete3(self):
        """Test case for delete3

        """
        pass

    def test_delete_all3(self):
        """Test case for delete_all3

        """
        pass

    def test_edit_multiple3(self):
        """Test case for edit_multiple3

        """
        pass

    def test_evaluate(self):
        """Test case for evaluate

        """
        pass

    def test_get7(self):
        """Test case for get7

        """
        pass

    def test_get8(self):
        """Test case for get8

        """
        pass

    def test_get_all3(self):
        """Test case for get_all3

        """
        pass

    def test_get_analytics(self):
        """Test case for get_analytics

        """
        pass

    def test_get_insights(self):
        """Test case for get_insights

        """
        pass

    def test_get_insights1(self):
        """Test case for get_insights1

        """
        pass

    def test_reset(self):
        """Test case for reset

        Delete associated anomalies and rerun detection till present  # noqa: E501
        """
        pass

    def test_run_task(self):
        """Test case for run_task

        """
        pass

    def test_validate_multiple(self):
        """Test case for validate_multiple

        """
        pass


if __name__ == '__main__':
    unittest.main()
