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
from dbpedia.api.research_project_api import ResearchProjectApi  # noqa: E501
from dbpedia.rest import ApiException


class TestResearchProjectApi(unittest.TestCase):
    """ResearchProjectApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.research_project_api.ResearchProjectApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_researchprojects_get(self):
        """Test case for researchprojects_get

        List all instances of ResearchProject  # noqa: E501
        """
        pass

    def test_researchprojects_id_get(self):
        """Test case for researchprojects_id_get

        Get a single ResearchProject by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
