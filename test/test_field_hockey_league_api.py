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
from dbpedia.api.field_hockey_league_api import FieldHockeyLeagueApi  # noqa: E501
from dbpedia.rest import ApiException


class TestFieldHockeyLeagueApi(unittest.TestCase):
    """FieldHockeyLeagueApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.field_hockey_league_api.FieldHockeyLeagueApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_fieldhockeyleagues_get(self):
        """Test case for fieldhockeyleagues_get

        List all instances of FieldHockeyLeague  # noqa: E501
        """
        pass

    def test_fieldhockeyleagues_id_get(self):
        """Test case for fieldhockeyleagues_id_get

        Get a single FieldHockeyLeague by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()