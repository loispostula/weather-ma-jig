#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
from datetime import datetime

from weathermajig import emoji
from weathermajig import cache

reload(sys)
sys.setdefaultencoding('utf8')

def output_verbose(forecast, place, **kargs):
    out = kargs

    current = forecast.get_current()
    today = forecast.get_today()

    temp = "%s°C" % current.get('temperature')
    time = datetime.fromtimestamp(current.get('time'))
    high = '%s°C' % today.get('temperatureMax')
    low = '%s°C' % today.get('temperatureMin')

    return '''
{date}
Forecast for {place}
---
CURRENTLY: {cur_temp}
HIGH: {high}
LOW: {low}
{icon} {conditions}
    '''.format(
            date = time.strftime('%a %D %r'),
            place = place,
            cur_temp = temp,
            high = high,
            low = low,
            icon = out.get('icon'),
            conditions = out.get('summary'),
        )

def output_short(out):

    return '%s: %s %s [%s]' % (
        out.get('place'),
        out.get('icon'),
        out.get('summary'),
        out.get('temp'))

def make(conf, forecast, place):
    current = forecast.get_current()
    out = {
        'place': "%s" % place,
        'temp': "%s°C" % int(round(current.get('temperature'))),
        'icon':  "%s"   % emoji.icon(current.get('icon')),
        'summary': "%s" % current.get('summary'),
    }

    if (conf.get('verbose')):
        out = output_verbose(forecast, conf.get('place'), **out)
    else:
        out = output_short(out)

    cache.write(conf, out)
    print(out)
