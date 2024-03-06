from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
app = Celery('myapp', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')
