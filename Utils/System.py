#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2018年4月14日
@author: Irony
@site: https://github.com/892768447
@email: 892768447@qq.com
@file: Utils.System
@description: 系统设置工具类
"""
import win32api
import win32con
import win32gui


__Author__ = 'By: Irony\nQQ: 892768447\nEmail: 892768447@qq.com'
__Copyright__ = 'Copyright (c) 2018 Irony'
__Version__ = 1.0


class _System:

    def setWallpaper(self, path):
        """设置壁纸"""
        key = win32api.RegOpenKey(
            win32con.HKEY_CURRENT_USER, 'Control Panel\\Desktop', 0, win32con.KEY_SET_VALUE)
        # 2拉伸,0居中,6适应,10填充,0平铺
        win32api.RegSetValueEx(key, 'WallpaperStyle', 0, win32con.REG_SZ, '2')
        # 1平铺,0拉伸或居中
        win32api.RegSetValueEx(key, 'TileWallpaper', 0, win32con.REG_SZ, '0')
        # 刷新桌面设置壁纸
        win32gui.SystemParametersInfo(
            win32con.SPI_SETDESKWALLPAPER, path, win32con.SPIF_SENDWININICHANGE)


System = _System()
