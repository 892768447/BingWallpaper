#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2018年4月14日
@author: Irony
@site: https://github.com/892768447
@email: 892768447@qq.com
@file: Utils.NetWork
@description: 网络工具类
"""
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest


__Author__ = 'By: Irony\nQQ: 892768447\nEmail: 892768447@qq.com'
__Copyright__ = 'Copyright (c) 2018 Irony'
__Version__ = 1.0


class _NetWork(QNetworkAccessManager):

    def __init__(self, *args, **kwargs):
        super(_NetWork, self).__init__(*args, **kwargs)
        self.finished.connect((self.onFinished))

    def onFinished(self, reply):
        # 请求完成后调用此函数
        req = reply.request()  # 获取之前构造的请求
        # 回调函数
        callback = req.attribute(QNetworkRequest.User + 3, None)
        if callback:
            callback(req, reply.readAll().data())
        reply.deleteLater()
        del reply


NetWork = _NetWork()
