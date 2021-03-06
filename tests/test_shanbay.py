#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from getpass import getpass
import sys

from src.shanbay import Shanbay

try:
    input = raw_input
except NameError:
    pass

username = input('\nUsername: ')
password = getpass()
shanbay = Shanbay(username, password, team_id=5878,
                  team_url='http://www.shanbay.com/team/detail/5878/')
encoding = sys.stdin.encoding


def test_members():
    """获取小组成员信息"""
    members = shanbay.members()
    print('')
    for member in members:
        print('{id}, {username}, {nickname}, {role}, {points}, {days}, '
              '{rate}, {checked_yesterday}, {checked}'.format(**member))


def test_dismiss():
    """踢人"""
    members = shanbay.members()
    print('')
    for member in members:
        print('{nickname}: {checked}'.format(**member))
        confirm = input('踢除？ (y/n)'.encode(encoding)).strip().lower()
        if confirm.startswith('y'):
            print('成功踢除' if shanbay.dismiss(member['id']) else '剔除失败')


def test_send_mail():
    """短信功能"""
    to = ['mozillazg']
    subject = '测试短信功能'
    message = '测试短信功能'
    shanbay.send_mail(to, subject, message)


def test_send_mail_2():
    """短信功能, 群发"""
    to = ['mozillazg', 'shootout']
    subject = '测试短信群发功能'
    message = '测试短信群发功能'
    shanbay.send_mail(to, subject, message)


def test_new_topic():
    """小组发帖"""
    title = 'hello world'
    content = 'hello world'
    shanbay.new_topic(title, content)


def test_reply_topic():
    """小组回帖"""
    content = 'reply'
    shanbay.reply_topic(250459, content)


def test_server_date():
    """服务器时间"""
    print('')
    print(shanbay.server_date())


def test_update_limit():
    """更新成员加入条件"""
    shanbay.update_limit(10)


def test_team_info():
    """小组信息"""
    print('')
    print(shanbay.team_info())
