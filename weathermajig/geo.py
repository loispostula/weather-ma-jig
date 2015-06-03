#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from geopy.geocoders import Nominatim
from urllib2 import urlopen
from contextlib import closing
import json

def get_loc(conf):
    lat = conf.get('lat')
    lng = conf.get('lng')
    if lat is None or lng is None:
        url = 'http://freegeoip.net/json/'
        with closing(urlopen(url)) as response:
            location = json.loads(response.read())
            city = location['city']
            lat = location['latitude']
            lng = location['longitude']
    return (city, lat, lng)
