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
import json
import os

from PyQt5.QtCore import QUrl, QTimer, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtNetwork import QNetworkRequest
from PyQt5.QtWidgets import QLabel, QHBoxLayout, QPushButton, QStackedLayout,\
    QApplication

from Utils.NetWork import NetWork
from Utils.Signals import Signals
from Widgets.PageView import PageView
from Widgets.StoryView import StoryView


__Author__ = 'By: Irony\nQQ: 892768447\nEmail: 892768447@qq.com'
__Copyright__ = 'Copyright (c) 2018 Irony'
__Version__ = 1.0


class MainView(QLabel):

    DirPath = 'Images'

    def __init__(self, *args, **kwargs):
        super(MainView, self).__init__(*args, **kwargs)
        self.setScaledContents(True)
        rect = QApplication.instance().desktop().availableGeometry()
        # 桌面大小的2/3
        self.resize(int(rect.width() * 2 / 3),
                    int(rect.height() * 2 / 3))
        # 布局
        layout = QHBoxLayout(self, spacing=0)
        layout.setContentsMargins(0, 0, 0, 0)
        Signals.setParent(self)
        NetWork.setParent(self)

        # 获取上一页图片的按钮
        layout.addWidget(QPushButton(
            self, objectName='previousButton', clicked=self.onPreviousPage))
        # 故事控件
        layout.addWidget(StoryView(self))
        # 层叠布局
        self.stackLayout = QStackedLayout(spacing=0)
        self.stackLayout.setContentsMargins(0, 0, 0, 0)
        layout.addLayout(self.stackLayout)

        # 获取下一页图片的按钮
        layout.addWidget(QPushButton(
            self, objectName='nextButton', clicked=self.onNextPage))

        # 当前日期的图片被下载
        Signals.currentImageAdded.connect(self.loadCurrentImage)
        # 单个item鼠标悬停离开信号
        Signals.imageHovered.connect(self.onImageHovered)

    def closeEvent(self, event):
        """关闭窗口时保存窗口的截图文件"""
        os.makedirs(self.DirPath, exist_ok=True)
        self.grab().save(os.path.join(self.DirPath, 'tmp.jpg'))
        super(MainView, self).closeEvent(event)

    def onImageHovered(self, hovered, image):
        self.setPixmap(QPixmap.fromImage(image) if hovered else self.oldImage)

    def onPreviousPage(self):
        """上一页"""
        index = self.stackLayout.currentIndex()
        if index > 0:
            index -= 1
            self.stackLayout.setCurrentIndex(index)

    def onNextPage(self):
        """下一页"""
        index = self.stackLayout.currentIndex()
        count = self.stackLayout.count() - 1
        if index < count:
            index += 1
            self.stackLayout.setCurrentIndex(index)

    def splist(self, src, length):
        # 等分列表
        return (src[i:i + length] for i in range(len(src)) if i % length == 0)

    def addImages(self, _, datas):
        """解析json数据并生成层叠2x2的网格页面"""
        try:
            imagesGroup = self.splist(json.loads(
                datas.decode()).get('images', []), 4)  # 每组4个
        except Exception as e:
            print(e)
            imagesGroup = []
        for images in imagesGroup:
            pageView = PageView(self)
            pageView.addImages(images)
            self.stackLayout.addWidget(pageView)
        # 设置当前索引
        self.stackLayout.setCurrentIndex(0)

    def loadCurrentImage(self, path):
        """加载当前日期的图片作为背景"""
        self.oldImage = QPixmap(path)
        self.setPixmap(self.oldImage)
        # 延迟1秒后显示
        QTimer.singleShot(1000, self.onShow)

    def onShow(self):
        self.setCursor(Qt.ArrowCursor)
        self.setVisible(True)
        Signals.splashClosed.emit(self)  # 通知关闭启动界面

    def initData(self):
        """加载api接口数据"""
        # 获取最近几天的
        url = 'https://cn.bing.com/HPImageArchive.aspx?format=js&idx=-1&n=8'
        NetWork.get(self.createRequest(url, self.addImages))
        # 获取之前的
        url = 'https://cn.bing.com/HPImageArchive.aspx?format=js&idx=7&n=8'
        NetWork.get(self.createRequest(url, self.addImages))
        # 获取每日故事
        url = 'http://cn.bing.com/cnhp/coverstory/'
        NetWork.get(self.createRequest(url, Signals.storyAdded.emit))

    def createRequest(self, url, callback):
        """创建网络请求"""
        req = QNetworkRequest(QUrl(url))
        # 回调函数用于加载图片显示
        req.setAttribute(QNetworkRequest.User + 3, callback)
        return req


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    MainView.DirPath = '../Images'
    w = MainView()
    w.show()
    sys.exit(app.exec_())
