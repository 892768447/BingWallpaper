#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Created on 2018年4月15日
# author: Irony
# site: https://github.com/892768447
# email: 892768447@qq.com
# file: Client
# description:
import cgitb
import sys


__Author__ = """By: Irony
QQ: 892768447
Email: 892768447@qq.com"""
__Copyright__ = 'Copyright (c) 2018 Irony'
__Version__ = 1.0


def start():
    from PyQt5.QtWidgets import QApplication
    from Widgets.MainView import MainView
    from Widgets.SplashView import SplashView
    from Utils.Style import Style
    app = QApplication(sys.argv)
    app.setApplicationName('必应壁纸')
    app.setStyleSheet(Style)

    # 启动图片
    splashView = SplashView()
    splashView.show()
    app.processEvents()

    w = MainView()
    w.setVisible(False)
#     w.show()
    w.initData()

    sys.exit(app.exec_())


class Catch:

    def catch(self, msg):
        from PyQt5.QtWidgets import QMessageBox
        QMessageBox.critical(None, 'Error', msg)
        raise SystemExit(0)

    write = catch


if __name__ == '__main__':
    try:
        sys.excepthook = cgitb.Hook(0, None, 5, Catch().catch, 'text')
        start()
    except SystemExit:
        pass
    except Exception as e:
        Catch().catch(str(e))
