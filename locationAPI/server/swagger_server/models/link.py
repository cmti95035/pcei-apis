# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Link(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, rel: object=None, href: object=None):  # noqa: E501
        """Link - a model defined in Swagger

        :param rel: The rel of this Link.  # noqa: E501
        :type rel: object
        :param href: The href of this Link.  # noqa: E501
        :type href: object
        """
        self.swagger_types = {
            'rel': object,
            'href': object
        }

        self.attribute_map = {
            'rel': 'rel',
            'href': 'href'
        }

        self._rel = rel
        self._href = href

    @classmethod
    def from_dict(cls, dikt) -> 'Link':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Link of this Link.  # noqa: E501
        :rtype: Link
        """
        return util.deserialize_model(dikt, cls)

    @property
    def rel(self) -> object:
        """Gets the rel of this Link.

        Describes the relationship between the URI and the resource.  # noqa: E501

        :return: The rel of this Link.
        :rtype: object
        """
        return self._rel

    @rel.setter
    def rel(self, rel: object):
        """Sets the rel of this Link.

        Describes the relationship between the URI and the resource.  # noqa: E501

        :param rel: The rel of this Link.
        :type rel: object
        """
        if rel is None:
            raise ValueError("Invalid value for `rel`, must not be `None`")  # noqa: E501

        self._rel = rel

    @property
    def href(self) -> object:
        """Gets the href of this Link.

        URI  # noqa: E501

        :return: The href of this Link.
        :rtype: object
        """
        return self._href

    @href.setter
    def href(self, href: object):
        """Sets the href of this Link.

        URI  # noqa: E501

        :param href: The href of this Link.
        :type href: object
        """
        if href is None:
            raise ValueError("Invalid value for `href`, must not be `None`")  # noqa: E501

        self._href = href
