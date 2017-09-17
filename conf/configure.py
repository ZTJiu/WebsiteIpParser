#!/usr/bin/env python
# -*- coding=utf-8 -*-
###########################################
# File  : conf.py
# Date  : 2017-09-16
# Author: Zhang Tianjiu
# Email : zhangtianjiu@vip.qq.com
###########################################

import os
import random
from yaml import load

config_path = os.path.join(os.path.dirname(__file__), 'conf.yaml')

with open(config_path, encoding='utf-8') as f:
    cont = f.read()

cf = load(cont)

def get_db_args():
    return cf.get('db')


def get_db_info():
    db = cf.get('db')
    user = db.get('user')
    password = db.get('password')
    host = db.get('host')
    port = db.get('port')
    db_name = db.get('db_name')

    return '{}:{}@{}:{}/{}'.format(user, password, host, port, db_name)


def get_broker_for_client():
    redis_info = cf.get('redis')
    host = redis_info.get('host')
    port = redis_info.get('port')
    password = redis_info.get('password')
    db = redis_info.get('broker')
    url = 'redis://:{}@{}:{}/{}'.format(password, host, port, db)

    return url


def get_redis_args():
    return cf.get('redis')


def get_timeout():
    return cf.get('time_out')


def get_crawl_interal():
    interal = random.randint(cf.get('min_crawl_interal'), cf.get('max_crawl_interal'))
    return interal


def get_excp_interal():
    return cf.get('excp_interal')


def get_max_repost_page():
    return cf.get('max_repost_page')


def get_max_search_page():
    return cf.get('max_search_page')


def get_max_home_page():
    return cf.get('max_home_page')


def get_max_comment_page():
    return cf.get('max_comment_page')


def get_max_retries():
    return cf.get('max_retries')


def get_broker_or_backend(types):
    """
    :param types: 类型，1表示中间人，2表示消息后端
    :return:
    """
    redis_info = cf.get('redis')
    host = redis_info.get('host')
    port = redis_info.get('port')
    password = redis_info.get('password')

    if types == 1:
        db = redis_info.get('broker')
    else:
        db = redis_info.get('backend')
    url = 'redis://:{}@{}:{}/{}'.format(password, host, port, db)

    return url


def get_code_password():
    return cf.get('yundama_passwd')


def get_running_mode():
    return cf.get('mode')


def get_share_host_count():
    return cf.get('share_host_count')


def get_cookie_expire_time():
    return cf.get('cookie_expire_time')

