# coding: utf-8

"""
    DBpedia

    This is the API of the DBpedia Ontology  # noqa: E501

    The version of the OpenAPI document: v0.0.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import dbpedia
from dbpedia.api.database_api import DatabaseApi  # noqa: E501
from dbpedia.rest import ApiException


class TestDatabaseApi(unittest.TestCase):
    """DatabaseApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.database_api.DatabaseApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_databases_get(self):
        """Test case for databases_get

        List all instances of Database  # noqa: E501
        """
        pass

    def test_databases_id_get(self):
        """Test case for databases_id_get

        Get a single Database by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()