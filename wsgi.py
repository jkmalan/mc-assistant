#!/usr/bin/env python

import sys
import site

site.addsitedir('/var/www/html/malandrakis/microcenter/private/lib/python3.7/site-packages')

sys.path.insert(0, '/var/www/html/malandrakis/microcenter/public')

from project.run import app as application
