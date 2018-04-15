"""
Created on 2018年4月15日
@author: Irony
@site: https://github.com/892768447
@email: 892768447@qq.com
@file: Widgets.ImageView
@description: 预览小图
"""
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QSpacerItem, QSizePolicy


__Author__ = 'By: Irony\nQQ: 892768447\nEmail: 892768447@qq.com'
__Copyright__ = 'Copyright (c) 2018 Irony'
__Version__ = 1.0


class ImageView(QLabel):

    def __init__(self, enddate, url, copyright,  # @ReservedAssignment
                 copyrightlink, hsh, *args, **kwargs):
        super(ImageView, self).__init__(*args, **kwargs)
        self.setScaledContents(True)  # 设置图片适应控件大小
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

    def setTitle(self, title, tip=''):
        """设置标题文字"""
        self.titleLabel.setText(title)
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

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = ImageView()
    w.show()
    w.setTitle('test', 'test').setPixmap('../Images/test.png')
    sys.exit(app.exec_())
