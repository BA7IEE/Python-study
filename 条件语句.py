# -*- coding:utf-8 -*-
# @FileName  :条件语句.py
# @Time      :2022/5/1 下午10:00
# @Author    :tungwerl

# 如果⽤户年龄⼤于等于18岁，即成年，输出"已经成年，可以上⽹"
"""
age = eval(input('请输入你的年龄：'))
if age >= 18:
    print('你已经成年，可以上网')
else:
    print('未成年不可以上网哦')
"""
# 多重判断
# 中国合法⼯作年龄为18-60岁，即如果年龄⼩于18的情况为童⼯，不合法；
# 如果年龄在18-60岁之间为合法⼯龄；⼤于60岁为法定退休年龄。
"""
age = int(input('请输入你的年龄：'))
if age < 18:
    print(f'你的年龄是{age}，你是童工哦')
elif age > 60:
    print(f'你的年龄是{age}，可以退休了')
else:
    print(f'你的年龄为{age}，是合法工龄')
"""

# if嵌套
#坐公交：如果有钱可以上⻋，没钱不能上⻋；上⻋后如果有空座，则可以坐下；如果没空座，就要站着。怎么书写程序？

"""
money = eval(input('如果有钱请输入数字 1，没钱请输入数字 0 ：'))
if money == 1:
    print('土豪请上车')
    seats = eval(input('请输入剩余座位数量：'))
    if seats == 0:
        print('既然没有座位，那你只能站着了')
    else:
        print('有座位，你请坐')
else:
    print('没钱就不能上车')
"""

# 猜拳游戏 (剪刀石头布)
import random

"""
computer = random.randint(0, 2)
player = eval(input('请出拳（0-剪刀，1-石头，2-布）：'))
player_win = (player == 0) and (computer == 2) or (player == 1) and (computer == 0) or (player == 2) and (computer == 1)
if player_win:
    print(f'你出的{player},电脑出的{computer}，你赢了')
elif computer == player:
    print('打平手')
else:
    print(f'你出的{player}，电脑出的{computer}，你输了')
"""

