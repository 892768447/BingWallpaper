"""
Created on 2018年4月15日
@author: Irony
@site: https://github.com/892768447
@email: 892768447@qq.com
@file: Widgets.ImageView
@description: 预览小图
"""


import os

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QSpacerItem, QSizePolicy

from Utils.NetWork import NetWork


__Author__ = 'By: Irony\nQQ: 892768447\nEmail: 892768447@qq.com'
__Copyright__ = 'Copyright (c) 2018 Irony'
__Version__ = 1.0


class ImageView(QLabel):

    DirPath = 'Images'

    def __init__(self, enddate, url, copyright,  # @ReservedAssignment
                 copyrightlink, hsh, *args, **kwargs):
        super(ImageView, self).__init__(*args, **kwargs)
        self.setScaledContents(True)  # 设置图片适应控件大小
        # 小图缩放的最大高度,2x2的格子,2排
        self._height = int(
            QApplication.instance().desktop().availableGeometry().height() / 2)
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
        title, author = copyright.split(' (')
        self.setTitle(title, author.replace(')', ''), copyrightlink)
        # 异步加载图片
        self.loadImage(enddate, url, hsh)

    def setTitle(self, title, tip='', link='#'):
        """设置标题文字"""
        self.titleLabel.setText(
            '<a style="text-decoration: none;" href="{1}">{0}</a>'.format(title, link))
        if tip:
            self.titleLabel.setToolTip(tip)
        return self

    def setPixmap(self, pixmap, height=270):
        """设置图片"""
        if isinstance(pixmap, str):
            # 加载图片并缩放
            pixmap = QPixmap.fromImage(QImage(pixmap).scaledToHeight(
                height, Qt.SmoothTransformation))
        elif isinstance(pixmap, QImage):
            pixmap = QPixmap.fromImage(pixmap)
        super(ImageView, self).setPixmap(pixmap)
        return self

    def loadImage(self, enddate, url, hsh):
        """从本地加载或者网络加载"""
        path = os.path.join(self.DirPath, hsh + '.jpg')
        if os.path.isfile(path):
            self.setPixmap(path, self._height)
            return
        os.makedirs(self.DirPath, exist_ok=True)
        # 网络加载
        NetWork.get(url, path, self.setPixmap)

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    ImageView.DirPath = '../Images'
    w = ImageView('20180416', 'http://cn.bing.com/az/hprichbg/rb/MozambiqueSandbar_ZH-CN12673484802_1920x1080.jpg',
                  '巴扎鲁托群岛，莫桑比克 (© Jody MacDonald/Offset)',
                  'http://www.bing.com/search?q=%E5%B7%B4%E6%89%8E%E9%B2%81%E6%89%98%E7%BE%A4%E5%B2%9B&form=hpcapt&mkt=zh-cn',
                  '62f395ac51112c59a394452d507d592a')
    w.show()
    sys.exit(app.exec_())
