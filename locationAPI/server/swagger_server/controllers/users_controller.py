import connexion
import six

from swagger_server import util


def users_get(zoneId, accessPointId=None):  # noqa: E501
    """users_get

    Users currently using a zone may be retrieved for sets of access points matching attribute in the request # noqa: E501

    :param zoneId: Zone ID
    :type zoneId: str
    :param accessPointId: Identifier of access point, reference \&quot;definitions\&quot; for string format
    :type accessPointId: str

    :rtype: object
    """
    return 'do some magic!'


def users_get_by_id(userId):  # noqa: E501
    """users_get_by_id

    Users currently using a zone may be retrieved for sets of access points matching attribute in the request # noqa: E501

    :param userId: User ID
    :type userId: str

    :rtype: object
    """
    return 'do some magic!'
