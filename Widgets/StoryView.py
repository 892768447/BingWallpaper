"""
Created on 2018年4月14日
@author: Irony
@site: https://github.com/892768447
@email: 892768447@qq.com
@file: Widgets.StoryView
@description: 故事页面
"""
import json

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem,\
    QSizePolicy

from Utils.Signals import Signals


__Author__ = 'By: Irony\nQQ: 892768447\nEmail: 892768447@qq.com'
__Copyright__ = 'Copyright (c) 2018 Irony'
__Version__ = 1.0


class StoryView(QWidget):

    def __init__(self, *args, **kwargs):
        super(StoryView, self).__init__(*args, **kwargs)
        layout = QVBoxLayout(self, spacing=0)
        layout.setContentsMargins(10, 30, 10, 60)  # 左上右下边距

        # 标题控件
        self.titleLabel = QLabel(self, wordWrap=True, objectName='titleLabel')
        layout.addWidget(self.titleLabel)

        # 中间拉伸
        layout.addSpacerItem(
            QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # 故事控件
        self.storyLabel = QLabel(self, wordWrap=True, objectName='storyLabel')
        layout.addWidget(self.storyLabel)

        # 信号槽
        Signals.storyAdded.connect(self._setStory)

    def setTitle(self, title, tip=''):
        """设置标题及提示文字"""
        self.titleLabel.setText(title)
        if tip:
            self.titleLabel.setToolTip(tip)
        return self

    def setStory(self, content, date='', provider='', country='', city='', continent=''):
        """设置故事内容及提示文字"""
        self.storyLabel.setText(content)
        tip = ''
        if date:
            tip += 'Date: %s\n' % date
        if provider:
            tip += 'Provider: %s\n' % provider
        if country:
            tip += 'Country: %s\n' % country
        if city:
            tip += 'City: %s\n' % city
        if continent:
            tip += 'Continent: %s' % continent
        if tip:
            self.storyLabel.setToolTip(tip)
        return self

    def _setStory(self, _, datas):
        """解析json数据"""
        try:
            datas = json.loads(datas.decode())
            content = datas.get('para1', '') + '\n' + datas.get('para2', '')
            date = datas.get('date', '')
            provider = datas.get('provider', '')
            country = datas.get('country', '')
            city = datas.get('city', '')
            continent = datas.get('continent', '')
            self.setTitle(datas.get('title', ''), datas.get('attribute', ''))
            self.setStory(content, date, provider, country, city, continent)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = StoryView()
    w.setTitle('翻滚吧，小海豚').setStory(
        '也许你不知道，今天是一年一度的“国家海豚日”，在这一天我们前往新西兰凯库拉的近海水域，那里有一群灰蒙蒙的海豚在南岛的太平洋海岸上冲浪，它们就是暗色斑纹海豚。暗色斑纹海豚目前只在南半球被发现，你可不要小瞧它们，它们可是非常擅长空中表演的高手。想看它们表演吗？一起来凯库拉小镇吧！',
        'April 14', '© Terry Whittaker/Alamy',
        '新西兰', '凯库拉', '大洋洲')
    w.show()
    sys.exit(app.exec_())
