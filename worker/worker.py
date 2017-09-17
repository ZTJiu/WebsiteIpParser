#!/usr/bin/env python
# -*- coding=utf-8 -*-
###########################################
# File  : worker.py
# Date  : 2017-09-13
# Author: Zhang Tianjiu
# Email : zhangtianjiu@vip.qq.com
###########################################

import os
from datetime import timedelta
from celery import Celery
from kombu import Exchange, Queue
from conf.configure import get_broker_or_backend
from celery import platforms

# allow celery worker started by root
platforms.C_FORCE_ROOT = True

worker_log_path = os.path.join(os.path.dirname(os.path.dirname(__file__))+'/logs', 'celery.log')
beat_log_path = os.path.join(os.path.dirname(os.path.dirname(__file__))+'/logs', 'beat.log')

tasks = ['tasks.login', 'tasks.user', 'tasks.search', 'tasks.home', 'tasks.comment', 'tasks.repost']

app = Celery('weibo_task', include=tasks, broker=get_broker_or_backend(1), backend=get_broker_or_backend(2))


