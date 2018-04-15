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
"""
