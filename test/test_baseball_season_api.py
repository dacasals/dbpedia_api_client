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
from dbpedia.api.baseball_season_api import BaseballSeasonApi  # noqa: E501
from dbpedia.rest import ApiException


class TestBaseballSeasonApi(unittest.TestCase):
    """BaseballSeasonApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.baseball_season_api.BaseballSeasonApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_baseballseasons_get(self):
        """Test case for baseballseasons_get

        List all instances of BaseballSeason  # noqa: E501
        """
        pass

    def test_baseballseasons_id_get(self):
        """Test case for baseballseasons_id_get

        Get a single BaseballSeason by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()