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
from dbpedia.models.beverage import Beverage  # noqa: E501
from dbpedia.rest import ApiException

class TestBeverage(unittest.TestCase):
    """Beverage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Beverage
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = dbpedia.models.beverage.Beverage()  # noqa: E501
        if include_optional :
            return Beverage(
                approximate_calories = [
                    1.337
                    ], 
                ingredient = [
                    None
                    ], 
                taste = [
                    '0'
                    ], 
                description = [
                    '0'
                    ], 
                type_of_yeast = [
                    '0'
                    ], 
                discontinued = [
                    '0'
                    ], 
                label = [
                    '0'
                    ], 
                type = [
                    '0'
                    ], 
                percentage_alcohol = [
                    56
                    ], 
                creator_of_dish = [
                    None
                    ], 
                serving_temperature = [
                    '0'
                    ], 
                introduced = [
                    '0'
                    ], 
                type_of_storage = [
                    '0'
                    ], 
                id = '0', 
                type_of_grain = [
                    '0'
                    ]
            )
        else :
            return Beverage(
        )

    def testBeverage(self):
        """Test Beverage"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()