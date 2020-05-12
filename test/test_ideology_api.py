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
from dbpedia.api.ideology_api import IdeologyApi  # noqa: E501
from dbpedia.rest import ApiException


class TestIdeologyApi(unittest.TestCase):
    """IdeologyApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.ideology_api.IdeologyApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_ideologys_get(self):
        """Test case for ideologys_get

        List all instances of Ideology  # noqa: E501
        """
        pass

    def test_ideologys_id_get(self):
        """Test case for ideologys_id_get

        Get a single Ideology by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()