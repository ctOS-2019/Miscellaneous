#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
定义总数number，循环节cycle和剩余数left
由[1,number]进行遍历，去掉第 cycle * n 个数，直到剩余left个

实现方式：
    以字典形式储存数，视为代号，每个代号对应一个自身序列，在首次循环时，代号与序列数相等
    在首次遍历时，不符合去除要求的数则存入临时字典（dict）中，等待下一次遍历，并设置新的编号
    每次删除都要确认是否达成left要求，为否，则继续
    重新读取临时字典，再次遍历。

    可以简单理解为，
    number 个人在一个窗口排队，每个人有一个序列号
    符合 number/cycle 余数为0的人离开队伍，否则排到队伍最后去，并获得一个新的序列号

    而在队伍刚形成时，每个人的序列号，与自己的位置相等
    随后逐个 +1
'''


def EndDraw(number, cycle, left):
    '''

    :param number: 总数
    :param cycle: 每cycle人删一个
    :param left: 需要的剩余人数
    :return: 列表list
    '''
    # 创建一个对应的字典
    source = {}
    for i in range(1, number + 1):
        source[str(i)] = i
    number += 1
    dict = {}  # 临时字典，储存每次循环时重新排队的人
    while len(source) > left:  # 未达到人数要求，则循环
        for key in list(source.keys()):
            if source[key] % cycle == 0:  # 符合要求，剔除队伍
                del source[key]
            else:
                dict[key] = number  # 否则，重新排队
                number += 1
            if len(source) == left:  # 达到要求，则结束循环
                dict = source
                break
        source = dict  # 从临时字典拿出数据
        dict = {}  # 清空临时字典
    return list(source.keys())


if __name__ == '__main__':
    print("实例场景：28名学生围成一圈，轮流从1至3报数，报到3淘汰，直到剩下两人为止")
    print("实例场景：则最后剩下的两人位置分别是")
    print("实例场景：EndDraw(number=28, cycle=3, left=2)")
    print(EndDraw(28, 3, 2))
