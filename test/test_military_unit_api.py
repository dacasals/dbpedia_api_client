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
from dbpedia.api.military_unit_api import MilitaryUnitApi  # noqa: E501
from dbpedia.rest import ApiException


class TestMilitaryUnitApi(unittest.TestCase):
    """MilitaryUnitApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.military_unit_api.MilitaryUnitApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_militaryunits_get(self):
        """Test case for militaryunits_get

        List all instances of MilitaryUnit  # noqa: E501
        """
        pass

    def test_militaryunits_id_get(self):
        """Test case for militaryunits_id_get

        Get a single MilitaryUnit by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()