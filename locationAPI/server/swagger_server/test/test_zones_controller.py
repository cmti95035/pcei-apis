# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestZonesController(BaseTestCase):
    """ZonesController integration test stubs"""

    def test_zones_by_id_get_aps(self):
        """Test case for zones_by_id_get_aps

        
        """
        query_string = [('interestRealm', 'interestRealm_example')]
        response = self.client.open(
            '/exampleAPI/location/v1/zones/{zoneId}/accessPoints'.format(zoneId='zoneId_example'),
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_zones_by_id_get_aps_by_id(self):
        """Test case for zones_by_id_get_aps_by_id

        
        """
        response = self.client.open(
            '/exampleAPI/location/v1/zones/{zoneId}/accessPoints/{accessPointId}'.format(zoneId='zoneId_example', accessPointId='accessPointId_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_zones_get(self):
        """Test case for zones_get

        
        """
        response = self.client.open(
            '/exampleAPI/location/v1/zones',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_zones_get_by_id(self):
        """Test case for zones_get_by_id

        
        """
        response = self.client.open(
            '/exampleAPI/location/v1/zones/{zoneId}'.format(zoneId='zoneId_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
