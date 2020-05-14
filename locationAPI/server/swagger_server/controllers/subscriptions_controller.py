import connexion
import six

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from swagger_server.models.user_tracking_subscription import UserTrackingSubscription  # noqa: E501
from swagger_server.models.zonal_traffic_subscription import ZonalTrafficSubscription  # noqa: E501
from swagger_server.models.zone_status_subscription import ZoneStatusSubscription  # noqa: E501
from swagger_server import util


def user_tracking_sub_del_by_id(subscriptionId):  # noqa: E501
    """user_tracking_sub_del_by_id

    This operation is used for retrieving an individual subscription to user tracking change notification. # noqa: E501

    :param subscriptionId: Subscription ID
    :type subscriptionId: str

    :rtype: None
    """
    return 'do some magic!'


def user_tracking_sub_get():  # noqa: E501
    """user_tracking_sub_get

    This operation is used for retrieving all active subscriptions to user tracking change notifications. # noqa: E501


    :rtype: InlineResponse2001
    """
    return 'do some magic!'


def user_tracking_sub_get_by_id(subscriptionId):  # noqa: E501
    """user_tracking_sub_get_by_id

    This operation is used for retrieving an individual subscription to user tracking change notification. # noqa: E501

    :param subscriptionId: Subscription ID
    :type subscriptionId: str

    :rtype: object
    """
    return 'do some magic!'


def user_tracking_sub_post(userTrackingSubscription):  # noqa: E501
    """user_tracking_sub_post

    This operation is used for creating a new subscription to user tracking change notification # noqa: E501

    :param userTrackingSubscription: User Tracking Subscription
    :type userTrackingSubscription: dict | bytes

    :rtype: object
    """
    if connexion.request.is_json:
        userTrackingSubscription = UserTrackingSubscription.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def user_tracking_sub_put_by_id(subscriptionId, userTrackingSubscription):  # noqa: E501
    """user_tracking_sub_put_by_id

    This operation is used for updating an individual subscription to user tracking change notification. # noqa: E501

    :param subscriptionId: Subscription ID
    :type subscriptionId: str
    :param userTrackingSubscription: User Tracking Subscription
    :type userTrackingSubscription: dict | bytes

    :rtype: object
    """
    if connexion.request.is_json:
        userTrackingSubscription = UserTrackingSubscription.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def zonal_traffic_sub_del_by_id(subscriptionId):  # noqa: E501
    """zonal_traffic_sub_del_by_id

    This operation is used for cancelling a subscription and stopping corresponding notifications. # noqa: E501

    :param subscriptionId: Subscription ID
    :type subscriptionId: str

    :rtype: None
    """
    return 'do some magic!'


def zonal_traffic_sub_get():  # noqa: E501
    """zonal_traffic_sub_get

    This operation is used for retrieving all active subscriptions to zonal traffic change notifications. # noqa: E501


    :rtype: InlineResponse200
    """
    return 'do some magic!'


def zonal_traffic_sub_get_by_id(subscriptionId):  # noqa: E501
    """zonal_traffic_sub_get_by_id

    This operation is used for updating an individual subscription to zonal traffic change notification. # noqa: E501

    :param subscriptionId: Subscription ID
    :type subscriptionId: str

    :rtype: object
    """
    return 'do some magic!'


def zonal_traffic_sub_post(zonalTrafficSubscription):  # noqa: E501
    """zonal_traffic_sub_post

    This operation is used for creating a new subscription to zonal traffic change notification. # noqa: E501

    :param zonalTrafficSubscription: Zonal Traffic Subscription
    :type zonalTrafficSubscription: dict | bytes

    :rtype: object
    """
    if connexion.request.is_json:
        zonalTrafficSubscription = ZonalTrafficSubscription.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def zonal_traffic_sub_put_by_id(subscriptionId, zonalTrafficSubscription):  # noqa: E501
    """zonal_traffic_sub_put_by_id

    This operation is used for updating an individual subscription to zonal traffic change notification. # noqa: E501

    :param subscriptionId: Subscription ID
    :type subscriptionId: str
    :param zonalTrafficSubscription: Zonal Traffic Subscription
    :type zonalTrafficSubscription: dict | bytes

    :rtype: object
    """
    if connexion.request.is_json:
        zonalTrafficSubscription = ZonalTrafficSubscription.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def zone_status_del_by_id(subscriptionId):  # noqa: E501
    """zone_status_del_by_id

    This operation is used for cancelling a subscription and stopping corresponding notifications. # noqa: E501

    :param subscriptionId: Subscription ID
    :type subscriptionId: str

    :rtype: None
    """
    return 'do some magic!'


def zone_status_get():  # noqa: E501
    """zone_status_get

    This operation is used for creating a new subscription to zone status change notification. # noqa: E501


    :rtype: InlineResponse2002
    """
    return 'do some magic!'


def zone_status_get_by_id(subscriptionId):  # noqa: E501
    """zone_status_get_by_id

    This operation is used for retrieving an individual subscription to zone status change notification. # noqa: E501

    :param subscriptionId: Subscription ID
    :type subscriptionId: str

    :rtype: object
    """
    return 'do some magic!'


def zone_status_post(zoneStatusSubscription):  # noqa: E501
    """zone_status_post

    This operation is used for creating a new subscription to zone status change notification. # noqa: E501

    :param zoneStatusSubscription: Zone Status Subscription
    :type zoneStatusSubscription: dict | bytes

    :rtype: object
    """
    if connexion.request.is_json:
        zoneStatusSubscription = ZoneStatusSubscription.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def zone_status_put_by_id(subscriptionId, zoneStatusSubscription):  # noqa: E501
    """zone_status_put_by_id

    This operation is used for updating an individual subscription to zone status change notification. # noqa: E501

    :param subscriptionId: Subscription ID
    :type subscriptionId: str
    :param zoneStatusSubscription: Zone Status Subscription
    :type zoneStatusSubscription: dict | bytes

    :rtype: object
    """
    if connexion.request.is_json:
        zoneStatusSubscription = ZoneStatusSubscription.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
