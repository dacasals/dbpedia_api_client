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
from dbpedia.api.race_horse_api import RaceHorseApi  # noqa: E501
from dbpedia.rest import ApiException


class TestRaceHorseApi(unittest.TestCase):
    """RaceHorseApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.race_horse_api.RaceHorseApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_racehorses_get(self):
        """Test case for racehorses_get

        List all instances of RaceHorse  # noqa: E501
        """
        pass

    def test_racehorses_id_get(self):
        """Test case for racehorses_id_get

        Get a single RaceHorse by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
