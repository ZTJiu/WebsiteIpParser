#!/usr/bin/env python
# -*- coding=utf-8 -*-
###########################################
# File  : dns_parser.py
# Date  : 2017-09-13
# Author: Zhang Tianjiu
# Email : zhangtianjiu@vip.qq.com
###########################################

import dns.resolver
from tasks import app

@app.task(ignore_result=True)
def parse_url(url):
    if (len(url) == 0):
        return
    website_ips = {}
    ips = []
    for ip in dns.resolver.query(url):
        ips.append(ip.to_text())
    if (len(ips) == 0):
        return
    website_ips[url] = ips
    app.send_task()

