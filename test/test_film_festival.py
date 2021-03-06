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
from dbpedia.models.film_festival import FilmFestival  # noqa: E501
from dbpedia.rest import ApiException

class TestFilmFestival(unittest.TestCase):
    """FilmFestival unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FilmFestival
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = dbpedia.models.film_festival.FilmFestival()  # noqa: E501
        if include_optional :
            return FilmFestival(
                opening_film = [
                    None
                    ], 
                number_of_people_attending = [
                    56
                    ], 
                end_date = [
                    '0'
                    ], 
                description = [
                    '0'
                    ], 
                caused_by = [
                    None
                    ], 
                closing_film = [
                    None
                    ], 
                label = [
                    '0'
                    ], 
                film = [
                    None
                    ], 
                type = [
                    '0'
                    ], 
                participant = [
                    '0'
                    ], 
                duration = [
                    1.337
                    ], 
                previous_event = [
                    None
                    ], 
                next_event = [
                    None
                    ], 
                id = '0', 
                following_event = [
                    None
                    ], 
                start_date = [
                    '0'
                    ]
            )
        else :
            return FilmFestival(
        )

    def testFilmFestival(self):
        """Test FilmFestival"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
