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
from dbpedia.api.ski_resort_api import SkiResortApi  # noqa: E501
from dbpedia.rest import ApiException


class TestSkiResortApi(unittest.TestCase):
    """SkiResortApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.ski_resort_api.SkiResortApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_skiresorts_get(self):
        """Test case for skiresorts_get

        List all instances of SkiResort  # noqa: E501
        """
        pass

    def test_skiresorts_id_get(self):
        """Test case for skiresorts_id_get

        Get a single SkiResort by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()