#######################################################
# 
# GeoObject.py
# Python implementation of the Class GeoObject
# Generated by Enterprise Architect
# Created on:      04-Nov-2020 4:27:04 PM
# Original author: natha
# 
#######################################################
from FreeTAKServer.model.RestMessages.RestEnumerations import RestEnumerations


class GeoObject:
    """a GeoObject is an element place on a map. It has a name, characteristics and an
    attitude.
    """
    uid = ""
# default constructor  def __init__(self):  
    # the kind of expected behavior of the GeoObject (e.g friendly, hostile, unknown).
    # Please see API documentation for a list of valid entries.
    attitude = ""
    # a GeoObject is the information that will determine which type will be placed on
    # the tak maps including his icon. Please see API documentation for a list of
    # valid entries.
    geoObject = ""
    # the way in which this geo information has been acquired. Please see API
    # documentation for a list of valid entries.
    how = ""
    # the angular distance of the geoobject from the earths equator expressed in
    # positive or negative float. (e.g 43.855682)
    #
    #  remember to set the display of your TAK in decimal cohordinates, where *West
    # 77.08* is equal to '-77.08' in the API
    latitude = ""
    # the angular distance of the geoobject from the meridian of the greenwich, UK
    # expressed in positive or negative float. (e.g -76.107.7998)
    longitude = ""
    # A string to ID the GeoObject on a map.
    name = ""
    # the length, expressed in seconds  until the point will stale out. Default is
    # 300 seconds or 5 minutes.
    timeout = ""