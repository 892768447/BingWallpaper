"""
Created on 2018年4月14日
@author: Irony
@site: https://github.com/892768447
@email: 892768447@qq.com
@file: Widgets.PageView
@description: 2 * 4个小图的预览页面
"""
from datetime import datetime, timedelta

from PyQt5.QtWidgets import QWidget, QGridLayout

from Utils.Signals import Signals
from Widgets.ImageView import ImageView


__Author__ = 'By: Irony\nQQ: 892768447\nEmail: 892768447@qq.com'
__Copyright__ = 'Copyright (c) 2018 Irony'
__Version__ = 1.0


class PageView(QWidget):

    def __init__(self, *args, **kwargs):
        super(PageView, self).__init__(*args, **kwargs)
        layout = QGridLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

    def addImages(self, images):
        """添加图片"""
        if not images:
            return
        for i, image in enumerate(images):
            # 获取需要的字段
            enddate = image.get(
                'enddate', (datetime.now() + timedelta(days=1 - i)).strftime('%Y%m%d'))
            url = image.get('url', '')
            copyright = image.get('copyright', '')  # @ReservedAssignment
            copyrightlink = image.get('copyrightlink', '')
            hsh = image.get('hsh', '')

            # 计算在格子中的位置
            # 列
            col = i % 2  # 0 or 1
            # 行
            row = int((i - col) / 2)

            # 添加图片到布局中
            self.layout().addWidget(
                ImageView(enddate, url, copyright, copyrightlink, hsh, self), row, col, 1, 1)
        # 发送信号通知主界面把自己添加到层叠布局中
        Signals.pageAdded.emit(self)
