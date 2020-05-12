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
from dbpedia.api.canal_api import CanalApi  # noqa: E501
from dbpedia.rest import ApiException


class TestCanalApi(unittest.TestCase):
    """CanalApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.canal_api.CanalApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_canals_get(self):
        """Test case for canals_get

        List all instances of Canal  # noqa: E501
        """
        pass

    def test_canals_id_get(self):
        """Test case for canals_id_get

        Get a single Canal by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()