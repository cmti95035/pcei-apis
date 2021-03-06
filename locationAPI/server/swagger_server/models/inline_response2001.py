# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class InlineResponse2001(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, notification_subscription_list: InlineResponse2001NotificationSubscriptionList=None):  # noqa: E501
        """InlineResponse2001 - a model defined in Swagger

        :param notification_subscription_list: The notification_subscription_list of this InlineResponse2001.  # noqa: E501
        :type notification_subscription_list: InlineResponse2001NotificationSubscriptionList
        """
        self.swagger_types = {
            'notification_subscription_list': InlineResponse2001NotificationSubscriptionList
        }

        self.attribute_map = {
            'notification_subscription_list': 'notificationSubscriptionList'
        }

        self._notification_subscription_list = notification_subscription_list

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2001':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_1 of this InlineResponse2001.  # noqa: E501
        :rtype: InlineResponse2001
        """
        return util.deserialize_model(dikt, cls)

    @property
    def notification_subscription_list(self) -> InlineResponse2001NotificationSubscriptionList:
        """Gets the notification_subscription_list of this InlineResponse2001.


        :return: The notification_subscription_list of this InlineResponse2001.
        :rtype: InlineResponse2001NotificationSubscriptionList
        """
        return self._notification_subscription_list

    @notification_subscription_list.setter
    def notification_subscription_list(self, notification_subscription_list: InlineResponse2001NotificationSubscriptionList):
        """Sets the notification_subscription_list of this InlineResponse2001.


        :param notification_subscription_list: The notification_subscription_list of this InlineResponse2001.
        :type notification_subscription_list: InlineResponse2001NotificationSubscriptionList
        """

        self._notification_subscription_list = notification_subscription_list
