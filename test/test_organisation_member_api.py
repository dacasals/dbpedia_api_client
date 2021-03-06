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
from dbpedia.api.organisation_member_api import OrganisationMemberApi  # noqa: E501
from dbpedia.rest import ApiException


class TestOrganisationMemberApi(unittest.TestCase):
    """OrganisationMemberApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.organisation_member_api.OrganisationMemberApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_organisationmembers_get(self):
        """Test case for organisationmembers_get

        List all instances of OrganisationMember  # noqa: E501
        """
        pass

    def test_organisationmembers_id_get(self):
        """Test case for organisationmembers_id_get

        Get a single OrganisationMember by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
