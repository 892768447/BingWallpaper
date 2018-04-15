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
from PyQt5.QtCore import QUrl
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest


__Author__ = 'By: Irony\nQQ: 892768447\nEmail: 892768447@qq.com'
__Copyright__ = 'Copyright (c) 2018 Irony'
__Version__ = 1.0


class _NetWork(QNetworkAccessManager):

    def __init__(self, *args, **kwargs):
        super(_NetWork, self).__init__(*args, **kwargs)
        self.finished.connect((self.onFinished))

    def get(self, url, path, callback):
        """构造get请求方法"""
        req = QNetworkRequest(QUrl(url))
        req.setAttribute(QNetworkRequest.User + 1, path)
        req.setAttribute(QNetworkRequest.User + 2, callback)
        super(_NetWork, self).get(req)

    def onFinished(self, reply):
        # 请求完成后调用此函数
        req = reply.request()  # 获取之前构造的请求
        # 保存路径
        path = req.attribute(QNetworkRequest.User + 1, None)
        # 回调函数
        callback = req.attribute(QNetworkRequest.User + 2, None)
        if path and callback:
            data = reply.readAll().data()
            with open(path, 'wb') as fp:
                fp.write(data)
            # 回调
            callback(path)
        reply.deleteLater()
        del reply

NetWork = _NetWork()
