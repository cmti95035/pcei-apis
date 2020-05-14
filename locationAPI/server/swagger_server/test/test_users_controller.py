# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestUsersController(BaseTestCase):
    """UsersController integration test stubs"""

    def test_users_get(self):
        """Test case for users_get

        
        """
        query_string = [('zoneId', 'zoneId_example'),
                        ('accessPointId', 'accessPointId_example')]
        response = self.client.open(
            '/exampleAPI/location/v1/users',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_get_by_id(self):
        """Test case for users_get_by_id

        
        """
        response = self.client.open(
            '/exampleAPI/location/v1/users/{userId}'.format(userId='userId_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
