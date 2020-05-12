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
from dbpedia.api.prime_minister_api import PrimeMinisterApi  # noqa: E501
from dbpedia.rest import ApiException


class TestPrimeMinisterApi(unittest.TestCase):
    """PrimeMinisterApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.prime_minister_api.PrimeMinisterApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_primeministers_get(self):
        """Test case for primeministers_get

        List all instances of PrimeMinister  # noqa: E501
        """
        pass

    def test_primeministers_id_get(self):
        """Test case for primeministers_id_get

        Get a single PrimeMinister by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()