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
from dbpedia.api.year_api import YearApi  # noqa: E501
from dbpedia.rest import ApiException


class TestYearApi(unittest.TestCase):
    """YearApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.year_api.YearApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_years_get(self):
        """Test case for years_get

        List all instances of Year  # noqa: E501
        """
        pass

    def test_years_id_get(self):
        """Test case for years_id_get

        Get a single Year by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()