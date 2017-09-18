#!/usr/bin/env python
# -*- coding=utf-8 -*-
###########################################
# File  : db_writer.py
# Date  : 2017-09-17
# Author: Zhang Tianjiu
# Email : zhangtianjiu@vip.qq.com
###########################################

from sqlalchemy import Table, MetaData, Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from conf import get_db_info

# 创建对象的基类:
Base = declarative_base()
# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://{}'.format(get_db_info))
metadata = MetaData()
DbSession = sessionmaker(bind=engine)

def init_table():
    ip_list_table = Table('ip_list',
                  metadata,
                  Column('ip', String(20), primary_key=True),
                  Column('website', String(60)))
    ip_list_table.create(engine)

init_table()

# 定义User对象:
class Ip(Base):
    # 表的名字:
    __tablename__ = 'ip_list'
    # 表的结构:
    ip = Column(String(20), primary_key=True)
    url = Column(String(40))


def insert_data(ip, website):
    # 创建session对象:
    session = DbSession()
    # 创建新User对象:
    new_ip = Ip(ip = ip, url = website)
    # 添加到session:
    session.add(new_ip)
    # 提交即保存到数据库:
    session.commit()
    # 关闭session:
    session.close()


__all__ = ['insert_data']
