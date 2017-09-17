#!/usr/bin/env python
# -*- coding=utf-8 -*-
###########################################
# File  : task_dispatcher.py
# Date  : 2017-09-17
# Author: Zhang Tianjiu
# Email : zhangtianjiu@vip.qq.com
###########################################

from celery import Celery

from conf import get_broker_for_client

broker = get_broker_for_client()
app = Celery(broker)

def get_websites():
    web_sites = []
    file_name = "../data/top_100_websites.txt"
    with open(file_name) as f:
        for line in f:
            web_sites.append(line.strip())
    return web_sites

def dispatch_task():
    web_sites = get_websites()
    for web_site in web_sites:
        app.send_task("worker.tasks.dns_parser", args=[web_site], queue="websites")

if __name__ == "__main__":
    dispatch_task();

