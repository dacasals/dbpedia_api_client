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
from dbpedia.models.biomolecule import Biomolecule  # noqa: E501
from dbpedia.rest import ApiException

class TestBiomolecule(unittest.TestCase):
    """Biomolecule unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Biomolecule
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = dbpedia.models.biomolecule.Biomolecule()  # noqa: E501
        if include_optional :
            return Biomolecule(
                entrezgene = [
                    '0'
                    ], 
                symbol = [
                    '0'
                    ], 
                description = [
                    '0'
                    ], 
                label = [
                    '0'
                    ], 
                type = [
                    '0'
                    ], 
                ensembl = [
                    '0'
                    ], 
                refseqprotein = [
                    '0'
                    ], 
                omim = [
                    56
                    ], 
                refseqmrna = [
                    '0'
                    ], 
                hgncid = [
                    '0'
                    ], 
                mgiid = [
                    '0'
                    ], 
                ec_number = [
                    '0'
                    ], 
                id = '0', 
                uniprot = [
                    '0'
                    ]
            )
        else :
            return Biomolecule(
        )

    def testBiomolecule(self):
        """Test Biomolecule"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()