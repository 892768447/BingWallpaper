#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QSplashScreen

from Utils.Signals import Signals


# Created on 2018年4月16日
# author: Irony
# site: https://github.com/892768447
# email: 892768447@qq.com
# file: Widgets.SplashView
# description: 启动画面
__Author__ = """By: Irony
QQ: 892768447
Email: 892768447@qq.com"""
__Copyright__ = 'Copyright (c) 2018 Irony'
__Version__ = 1.0


class SplashView(QSplashScreen):

    DirPath = 'Images'

    def __init__(self):
        self._closed = False
        # 加载临时截图文件
        path = os.path.join(self.DirPath, 'tmp.jpg')
        if os.path.isfile(path):
            super(SplashView, self).__init__(QPixmap(path))
        else:
            super(SplashView, self).__init__()
        Signals.splashClosed.connect(self.onClose)
        self.showMessage('正在加载网络数据...', Qt.AlignRight |
                         Qt.AlignBottom, Qt.white)

    def onClose(self, widget):
        if not self._closed:
            self._closed = True
            self.finish(widget)
