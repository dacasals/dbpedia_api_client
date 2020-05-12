# coding: utf-8

"""
    DBpedia

    This is the API of the DBpedia Ontology  # noqa: E501

    The version of the OpenAPI document: v0.0.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import dbpedia
from dbpedia.models.boxing_category import BoxingCategory  # noqa: E501
from dbpedia.rest import ApiException

class TestBoxingCategory(unittest.TestCase):
    """BoxingCategory unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BoxingCategory
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = dbpedia.models.boxing_category.BoxingCategory()  # noqa: E501
        if include_optional :
            return BoxingCategory(
                number_of_players = [
                    56
                    ], 
                number_of_professionals = [
                    56
                    ], 
                number_of_clubs = [
                    56
                    ], 
                current_world_champion = [
                    None
                    ], 
                first_olympic_event = [
                    None
                    ], 
                footedness = [
                    None
                    ], 
                description = [
                    '0'
                    ], 
                equipment = [
                    None
                    ], 
                id = '0', 
                label = [
                    '0'
                    ], 
                number_of_people_licensed = [
                    56
                    ], 
                type = [
                    '0'
                    ]
            )
        else :
            return BoxingCategory(
        )

    def testBoxingCategory(self):
        """Test BoxingCategory"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()