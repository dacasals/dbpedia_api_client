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
from dbpedia.api.television_show_api import TelevisionShowApi  # noqa: E501
from dbpedia.rest import ApiException


class TestTelevisionShowApi(unittest.TestCase):
    """TelevisionShowApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.television_show_api.TelevisionShowApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_televisionshows_get(self):
        """Test case for televisionshows_get

        List all instances of TelevisionShow  # noqa: E501
        """
        pass

    def test_televisionshows_id_get(self):
        """Test case for televisionshows_id_get

        Get a single TelevisionShow by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()