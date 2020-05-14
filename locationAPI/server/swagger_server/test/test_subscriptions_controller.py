# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from swagger_server.models.user_tracking_subscription import UserTrackingSubscription  # noqa: E501
from swagger_server.models.zonal_traffic_subscription import ZonalTrafficSubscription  # noqa: E501
from swagger_server.models.zone_status_subscription import ZoneStatusSubscription  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSubscriptionsController(BaseTestCase):
    """SubscriptionsController integration test stubs"""

    def test_user_tracking_sub_del_by_id(self):
        """Test case for user_tracking_sub_del_by_id

        
        """
        response = self.client.open(
            '/exampleAPI/location/v1/subscriptions/userTracking/{subscriptionId}'.format(subscriptionId='subscriptionId_example'),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_tracking_sub_get(self):
        """Test case for user_tracking_sub_get

        
        """
        response = self.client.open(
            '/exampleAPI/location/v1/subscriptions/userTracking',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_tracking_sub_get_by_id(self):
        """Test case for user_tracking_sub_get_by_id

        
        """
        response = self.client.open(
            '/exampleAPI/location/v1/subscriptions/userTracking/{subscriptionId}'.format(subscriptionId='subscriptionId_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_tracking_sub_post(self):
        """Test case for user_tracking_sub_post

        
        """
        userTrackingSubscription = UserTrackingSubscription()
        response = self.client.open(
            '/exampleAPI/location/v1/subscriptions/userTracking',
            method='POST',
            data=json.dumps(userTrackingSubscription),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_tracking_sub_put_by_id(self):
        """Test case for user_tracking_sub_put_by_id

        
        """
        userTrackingSubscription = UserTrackingSubscription()
        response = self.client.open(
            '/exampleAPI/location/v1/subscriptions/userTracking/{subscriptionId}'.format(subscriptionId='subscriptionId_example'),
            method='PUT',
            data=json.dumps(userTrackingSubscription),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_zonal_traffic_sub_del_by_id(self):
        """Test case for zonal_traffic_sub_del_by_id

        
        """
        response = self.client.open(
            '/exampleAPI/location/v1/subscriptions/zonalTraffic/{subscriptionId}'.format(subscriptionId='subscriptionId_example'),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_zonal_traffic_sub_get(self):
        """Test case for zonal_traffic_sub_get

        
        """
        response = self.client.open(
            '/exampleAPI/location/v1/subscriptions/zonalTraffic',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_zonal_traffic_sub_get_by_id(self):
        """Test case for zonal_traffic_sub_get_by_id

        
        """
        response = self.client.open(
            '/exampleAPI/location/v1/subscriptions/zonalTraffic/{subscriptionId}'.format(subscriptionId='subscriptionId_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_zonal_traffic_sub_post(self):
        """Test case for zonal_traffic_sub_post

        
        """
        zonalTrafficSubscription = ZonalTrafficSubscription()
        response = self.client.open(
            '/exampleAPI/location/v1/subscriptions/zonalTraffic',
            method='POST',
            data=json.dumps(zonalTrafficSubscription),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_zonal_traffic_sub_put_by_id(self):
        """Test case for zonal_traffic_sub_put_by_id

        
        """
        zonalTrafficSubscription = ZonalTrafficSubscription()
        response = self.client.open(
            '/exampleAPI/location/v1/subscriptions/zonalTraffic/{subscriptionId}'.format(subscriptionId='subscriptionId_example'),
            method='PUT',
            data=json.dumps(zonalTrafficSubscription),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_zone_status_del_by_id(self):
        """Test case for zone_status_del_by_id

        
        """
        response = self.client.open(
            '/exampleAPI/location/v1/subscriptions/zoneStatus/{subscriptionId}'.format(subscriptionId='subscriptionId_example'),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_zone_status_get(self):
        """Test case for zone_status_get

        
        """
        response = self.client.open(
            '/exampleAPI/location/v1/subscriptions/zonalStatus',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_zone_status_get_by_id(self):
        """Test case for zone_status_get_by_id

        
        """
        response = self.client.open(
            '/exampleAPI/location/v1/subscriptions/zoneStatus/{subscriptionId}'.format(subscriptionId='subscriptionId_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_zone_status_post(self):
        """Test case for zone_status_post

        
        """
        zoneStatusSubscription = ZoneStatusSubscription()
        response = self.client.open(
            '/exampleAPI/location/v1/subscriptions/zonalStatus',
            method='POST',
            data=json.dumps(zoneStatusSubscription),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_zone_status_put_by_id(self):
        """Test case for zone_status_put_by_id

        
        """
        zoneStatusSubscription = ZoneStatusSubscription()
        response = self.client.open(
            '/exampleAPI/location/v1/subscriptions/zoneStatus/{subscriptionId}'.format(subscriptionId='subscriptionId_example'),
            method='PUT',
            data=json.dumps(zoneStatusSubscription),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
