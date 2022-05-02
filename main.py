# -*- coding:utf-8 -*-
# @FileName  :条件语句.py
# @Time      :2022/5/1 下午10:00
# @Author    :tungwerl
def eval_help():
    '''
    eval() 函数可以去掉字符串的引号
    :return: 返回去掉引号的数字（int）
    '''
    num = eval(input('请输入数字：'))
    print(num)
    return num


if __name__ == '__main__':

    pass