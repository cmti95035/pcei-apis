import connexion
import six

from swagger_server import util


def zones_by_id_get_aps(zoneId, interestRealm=None):  # noqa: E501
    """zones_by_id_get_aps

    Access point status can be retrieved for sets of access points matching attribute in the request. # noqa: E501

    :param zoneId: Zone ID
    :type zoneId: str
    :param interestRealm: Interest realm of access point (e.g. geographical area, a type of industry etc.).
    :type interestRealm: str

    :rtype: object
    """
    return 'do some magic!'


def zones_by_id_get_aps_by_id(zoneId, accessPointId):  # noqa: E501
    """zones_by_id_get_aps_by_id

    Access point status can be retrieved for sets of access points matching attribute in the request. # noqa: E501

    :param zoneId: Zone ID
    :type zoneId: str
    :param accessPointId: Access Point ID
    :type accessPointId: str

    :rtype: object
    """
    return 'do some magic!'


def zones_get():  # noqa: E501
    """zones_get

    Used to get a list of identifiers for zones authorized for use by the application. # noqa: E501


    :rtype: object
    """
    return 'do some magic!'


def zones_get_by_id(zoneId):  # noqa: E501
    """zones_get_by_id

    Used to get the status of a zone. # noqa: E501

    :param zoneId: Zone ID
    :type zoneId: str

    :rtype: object
    """
    return 'do some magic!'
