# -*- coding:utf-8 -*-
# @FileName  :循环.py
# @Time      :2022/5/2 下午5:01
# @Author    :tungwerl

# 假如我有个⼥朋友，有⼀天我们闹⽭盾⽣⽓了，⼥朋友说：道歉，说100遍“媳妇⼉，我错了”。这个时候程序员会怎么做？
def eg_1():
    count = 0
    while count < 100:
        print('媳妇⼉，我错了')
        count += 1
    print(f'媳妇儿，我说完{count}遍了')

# 计算1-100的和，即1 + 2 + 3 + 4 + ... + 100
def eg_2():
    count = 0
    result = 0
    while count <= 100:
        result += count
        count += 1
    print(f'1到{count - 1}的和等于{result}')

# 计算1-100偶数累加和方法1
def eg_2():
    count = 0
    result = 0
    while count < 100:
        count += 1
        if count % 2 == 0:
            result += count
    print(result)

# 计算1-100偶数累加和方法2
def eg_3():
    count = 0
    result = 0
    while count <= 100:
        result += count
        count += 2
    print(result)
