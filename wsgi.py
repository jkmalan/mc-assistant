#!/usr/bin/env python

import sys

sys.path.insert(0, '/var/www/html/malandrakis/microcenter/public')

from project.app import create_app

application = create_app()
