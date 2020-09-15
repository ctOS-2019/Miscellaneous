#!/usr/bin/env python
# -*- coding: utf-8 -*-
def ConsoleColor(text, fcolor=False, bcolor=False, h=False, u=False, s=False, f=False):
    """
    为pyCharm的控制台输出加上颜色

    :param text: 待处理文本
    :param fcolor: 前景色
    :param bcolor: 背景色
    :param h: 高亮/加粗（默认否）
    :param u: 下划线（默认否）
    :param s: 闪烁（默认否）
    :param f: 反显（默认否）
    :return: 返回样式设置
    """
    fcdict = {'white': '30', 'red': '31', 'green': '32', 'yellow': '33', 'blue': '34', 'purple': '35',
              'turquoise': '36', 'gray': '73'}
    bcdict = {'white': '40', 'red': '41', 'green': '42', 'yellow': '43', 'blue': '44', 'purple': '45',
              'turquoise': '46', 'gray': '47'}
    style = ''
    style_list = []
    if fcolor or bcolor or h or u or s or f:
        if h:
            style_list.append('1')
        if u:
            style_list.append('4')
        if s:
            style_list.append('5')
        if f:
            style_list.append('7')
        if fcolor:
            style_list.append(fcdict[fcolor])
        if bcolor:
            style_list.append(bcdict[bcolor])
        style = ';'.join(style_list)
    start = '\033['
    end = '\033[0m'
    return start + style + 'm' + text + end


if __name__ == '__main__':
    print(ConsoleColor('HelloWorld', fcolor='red', u=True, s=True))
