#!/usr/bin/env python
# -*- coding=utf-8 -*-
###########################################
# File  : worker.py
# Date  : 2017-09-13
# Author: Zhang Tianjiu
# Email : zhangtianjiu@vip.qq.com
###########################################

import os
from celery import Celery
#from kombu import Exchange, Queue
from conf.configure import get_broker_or_backend
#from celery import platforms

# allow celery worker started by root
#platforms.C_FORCE_ROOT = True

worker_log_path = os.path.join(os.path.dirname(os.path.dirname(__file__))+'../logs', 'celery.log')
beat_log_path = os.path.join(os.path.dirname(os.path.dirname(__file__))+'../logs', 'beat.log')

tasks = ['tasks.dns_parser', 'tasks.pinger']

app = Celery('website_parser', include=tasks, broker=get_broker_or_backend(1), backend=get_broker_or_backend(2))

app.conf.update(CELERY_DEFAULT_QUEUE='default_queue',
                CELERYD_LOG_FILE=worker_log_path,
                CELERYBEAT_LOG_FILE=beat_log_path)


