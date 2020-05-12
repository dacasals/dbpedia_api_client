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
from dbpedia.api.church_api import ChurchApi  # noqa: E501
from dbpedia.rest import ApiException


class TestChurchApi(unittest.TestCase):
    """ChurchApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.church_api.ChurchApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_churchs_get(self):
        """Test case for churchs_get

        List all instances of Church  # noqa: E501
        """
        pass

    def test_churchs_id_get(self):
        """Test case for churchs_id_get

        Get a single Church by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()