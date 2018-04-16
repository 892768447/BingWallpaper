#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created on 2018年4月15日
# author: Irony
# site: https://github.com/892768447
# email: 892768447@qq.com
# file: Utils.Style
# description:

__Author__ = """By: Irony
QQ: 892768447
Email: 892768447@qq.com"""
__Copyright__ = 'Copyright (c) 2018 Irony'
__Version__ = 1.0

Style = """
QLabel {
    color: white;
}

StoryView {
    min-width: 300px;
    max-width: 300px;
}
StoryView > QLabel {
    font-size: 20px;
}

ImageView > #titleLabel {
    min-height: 24px;
    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 70), stop:1 rgba(0, 0, 0, 50));
}

#childWidget {
    background-color: rgba(255, 255, 255, 100);
}

#previousButton {
    color: white;
    qproperty-text: "3";
    font-size: 60px;
    font-family: "webdings";
    border: none;
    background: transparent;
}

#nextButton {
    color: white;
    qproperty-text: "4";
    font-size: 60px;
    font-family: "webdings";
    border: none;
    background: transparent;
}

#previousButton:hover,#nextButton:hover {
    background: rgba(255, 255, 255, 100);
}

QMenu {
    background-color: white;
    border: none;
}
QMenu::item {
    padding:8px 32px;
    background-color: transparent;
}
QMenu::item:selected {
    color: black;
    background-color: rgba(0, 0, 0, 50);
}
"""
