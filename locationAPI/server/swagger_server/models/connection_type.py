# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ConnectionType(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    FEMTO = "Femto"
    LTE_FEMTO = "LTE-femto"
    SMALLCELL = "Smallcell"
    LTE_SMALLCELL = "LTE-smallcell"
    WIFI = "Wifi"
    PICO = "Pico"
    MICRO = "Micro"
    MACRO = "Macro"
    WIMAX = "Wimax"
    UNKNOWN = "Unknown"

    def __init__(self):  # noqa: E501
        """ConnectionType - a model defined in Swagger

        """
        self.swagger_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'ConnectionType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ConnectionType of this ConnectionType.  # noqa: E501
        :rtype: ConnectionType
        """
        return util.deserialize_model(dikt, cls)
