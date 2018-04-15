"""
Created on 2018年4月15日
@author: Irony
@site: https://github.com/892768447
@email: 892768447@qq.com
@file: Widgets.ImageView
@description: 预览小图
"""


from datetime import datetime
import os

from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtNetwork import QNetworkRequest
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QSpacerItem, QSizePolicy,\
    QApplication

from Utils.NetWork import NetWork
from Utils.Signals import Signals


__Author__ = 'By: Irony\nQQ: 892768447\nEmail: 892768447@qq.com'
__Copyright__ = 'Copyright (c) 2018 Irony'
__Version__ = 1.0


class ImageView(QLabel):

    DirPath = 'Images'

    def __init__(self, enddate, url, copyright,  # @ReservedAssignment
                 copyrightlink, hsh, *args, **kwargs):
        super(ImageView, self).__init__(*args, **kwargs)
        self._image = None
        self.setOpenExternalLinks(True)
        self.setScaledContents(True)  # 设置图片适应控件大小
        self.setCursor(Qt.PointingHandCursor)
        layout = QVBoxLayout(self, spacing=0)
        layout.setContentsMargins(2, 2, 2, 2)
        # 拉伸
        layout.addSpacerItem(
            QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        # 底部标题
        self.titleLabel = QLabel(
            self, wordWrap=True, alignment=Qt.AlignRight | Qt.AlignBottom,
            objectName='titleLabel')
        layout.addWidget(self.titleLabel)
        # 设置文字和加载图片
        try:
            title, author = copyright.split('(')
        except:
            title, author = copyright.split('（')
        self.setTitle(title, author.replace(')', '').replace(
            '）', ''), copyrightlink)
        # 异步加载图片
        self.loadImage(enddate, url, hsh)

    def setTitle(self, title, tip='', link='#'):
        """设置标题文字"""
        self.titleLabel.setText(
            '<a style="text-decoration: none;color: white;" href="{1}">{0}</a>'.format(title, link))
        if tip:
            self.titleLabel.setToolTip(tip)
        return self

    def resizeEvent(self, event):
        super(ImageView, self).resizeEvent(event)
        if self._image and not self.pixmap():  # 没有设置图片
            self.setPixmap(QPixmap.fromImage(  # 设置缩放图片
                self._image.scaled(self.width(), self.height(), transformMode=Qt.SmoothTransformation)))

    def mousePressEvent(self, event):
        """鼠标单击预览"""
        super(ImageView, self).mousePressEvent(event)
        Signals.imageHovered.emit(True, self._image)

    def mouseDoubleClickEvent(self, event):
        """鼠标双击则应用壁纸"""
        super(ImageView, self).mouseDoubleClickEvent(event)

    def setPixmap(self, pixmap):
        """设置图片"""
        if isinstance(pixmap, str):
            self._image = QImage(pixmap)  # 先加载图片并不显示
            return self
        super(ImageView, self).setPixmap(pixmap)
        return self

    def loadImage(self, enddate, url, hsh):
        """从本地加载或者网络加载"""
        path = os.path.join(self.DirPath, hsh + '.jpg')
        if os.path.isfile(path) and os.path.getsize(path) > 100:
            if enddate == datetime.now().strftime('%Y%m%d'):  # 今日
                Signals.currentImageAdded.emit(path)
            self.setPixmap(path)
            return
        os.makedirs(self.DirPath, exist_ok=True)
        # 网络加载
        NetWork.get(self.createRequest(
            enddate, 'http://cn.bing.com' + url, path))

    def _setPixmap(self, req, data):
        """回调函数"""
        enddate = req.attribute(QNetworkRequest.User + 1, '')
        path = req.attribute(QNetworkRequest.User + 2, '')
        # 写入文件
        with open(path, 'wb') as fp:
            fp.write(data)
        if enddate == datetime.now().strftime('%Y%m%d'):  # 今日
            Signals.currentImageAdded.emit(path)
        self.setPixmap(path)

    def createRequest(self, enddate, url, path):
        """创建网络请求"""
        req = QNetworkRequest(QUrl(url))
        # 日期
        req.setAttribute(QNetworkRequest.User + 1, enddate)
        # 图片储存路径
        req.setAttribute(QNetworkRequest.User + 2, path)
        # 回调函数用于加载图片显示
        req.setAttribute(QNetworkRequest.User + 3, self._setPixmap)
        return req


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ImageView.DirPath = '../Images'
    w = ImageView('20180416', '/az/hprichbg/rb/MozambiqueSandbar_ZH-CN12673484802_1920x1080.jpg',
                  '巴扎鲁托群岛，莫桑比克 (© Jody MacDonald/Offset)',
                  'http://www.bing.com/search?q=%E5%B7%B4%E6%89%8E%E9%B2%81%E6%89%98%E7%BE%A4%E5%B2%9B&form=hpcapt&mkt=zh-cn',
                  '62f395ac51112c59a394452d507d592a')
    w.show()
    sys.exit(app.exec_())
