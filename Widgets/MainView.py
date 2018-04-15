#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2018年4月14日
@author: Irony
@site: https://github.com/892768447
@email: 892768447@qq.com
@file: Widgets.MainView
@description: 主界面
"""
from PyQt5.QtWidgets import QLabel, QHBoxLayout, QPushButton, QStackedLayout

from Utils.NetWork import NetWork
from Utils.Signals import Signals
from Widgets.StoryView import StoryView


__Author__ = 'By: Irony\nQQ: 892768447\nEmail: 892768447@qq.com'
__Copyright__ = 'Copyright (c) 2018 Irony'
__Version__ = 1.0


class MainView(QLabel):

    def __init__(self, *args, **kwargs):
        super(MainView, self).__init__(*args, **kwargs)
        layout = QHBoxLayout(self, spacing=0)
        layout.setContentsMargins(0, 0, 0, 0)
        Signals.setParent(self)
        NetWork.setParent(self)

        # 获取上一页图片的按钮
        layout.addWidget(QPushButton(self, objectName='previousButton'))
        # 故事控件
        layout.addWidget(StoryView(self))
        # 层叠布局
        self.stackLayout = QStackedLayout(spacing=0)
        self.stackLayout.setContentsMargins(0, 80, 0, 40)
        layout.addLayout(self.stackLayout)
        # 绑定添加新页面的信号槽
        Signals.pageAdded.connect(self.stackLayout.addWidget)

        # 获取下一页图片的按钮
        layout.addWidget(QPushButton(self, objectName='nextButton'))
    
    def _initData(self):
        """加载api接口数据"""

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = MainView()
    w.show()
    sys.exit(app.exec_())
