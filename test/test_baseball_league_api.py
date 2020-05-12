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
from dbpedia.api.baseball_league_api import BaseballLeagueApi  # noqa: E501
from dbpedia.rest import ApiException


class TestBaseballLeagueApi(unittest.TestCase):
    """BaseballLeagueApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.baseball_league_api.BaseballLeagueApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_baseballleagues_get(self):
        """Test case for baseballleagues_get

        List all instances of BaseballLeague  # noqa: E501
        """
        pass

    def test_baseballleagues_id_get(self):
        """Test case for baseballleagues_id_get

        Get a single BaseballLeague by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()