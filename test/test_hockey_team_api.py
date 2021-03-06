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
from dbpedia.api.hockey_team_api import HockeyTeamApi  # noqa: E501
from dbpedia.rest import ApiException


class TestHockeyTeamApi(unittest.TestCase):
    """HockeyTeamApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.hockey_team_api.HockeyTeamApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_hockeyteams_get(self):
        """Test case for hockeyteams_get

        List all instances of HockeyTeam  # noqa: E501
        """
        pass

    def test_hockeyteams_id_get(self):
        """Test case for hockeyteams_id_get

        Get a single HockeyTeam by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
