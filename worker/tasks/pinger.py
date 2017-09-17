#!/usr/bin/env python
# -*- coding=utf-8 -*-
###########################################
# File  : pinger.py
# Date  : 2017-09-17
# Author: Zhang Tianjiu
# Email : zhangtianjiu@vip.qq.com
###########################################

import pyping
from worker import app
from db_writer import insert_data

@app.task(ignore_result=True)
def ping(website, ips):
    for ip in ips:
        response = pyping.ping(ip, count=2)
        if response.ret_code is 0:
            insert_data(website, ip)

