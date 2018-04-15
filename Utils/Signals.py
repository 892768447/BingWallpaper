"""
Created on 2018年4月14日
@author: Irony
@site: https://github.com/892768447
@email: 892768447@qq.com
@file: Utils.Signals
@description: 信号 
"""
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QWidget


__Author__ = 'By: Irony\nQQ: 892768447\nEmail: 892768447@qq.com'
__Copyright__ = 'Copyright (c) 2018 Irony'
__Version__ = 1.0


class _Signals(QObject):

    # 添加新页
    pageAdded = pyqtSignal(QWidget)

Signals = _Signals()
