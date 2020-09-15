'''
定义总数number，循环节cycle和剩余数left
由[1,number]进行遍历，去掉第 cycle * n 个数，直到剩余left个

实现方式：
    以字典形式储存数，视为代号，每个代号对应一个自身序列，在首次循环时，代号与序列数相等
    在首次遍历时，不符合去除要求的数则存入临时字典（dict）中，等待下一次遍历，并设置新的编号
    每次删除都要确认是否达成left要求，为否，则继续
    重新读取临时字典，再次遍历。
'''
def EndDraw(number,cycle,left):
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
    # 符合条件时，遍历字典筛选
    number += 1
    dict = {}
    while len(source) > left:
        for key in list(source.keys()):
            if source[key] % cycle == 0:
                del source[key]
            else:
                dict[key] = number
                number += 1
            if len(source) == left:
                dict = source
                break
        source = dict
        dict = {}
    return list(source.keys())

if __name__ == '__main__':
    print("实例场景：28名学生围成一圈，轮流从1至3报数，报到3淘汰，直到剩下两人为止")
    print("实例场景：则最后剩下的两人位置分别是")
    print(EndDraw(28,3,2))