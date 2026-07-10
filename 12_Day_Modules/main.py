from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g
print(fullname('Asabneh','Yetayeh'))
print(total(1, 9))
mass = 100
print(mass)
weight = mass * g
print(weight)
print(p)
print(p['firstname'])

import os

print("当前工作目录：", os.getcwd())  # 当前工作目录： D:\Study\30-Days-of-Python-ssy\30-Days-Of-Python\12_Day_Modules
print("脚本文件：", __file__)  # 脚本文件： d:\Study\30-Days-of-Python-ssy\30-Days-Of-Python\12_Day_Modules\main.py
print("脚本所在目录：", os.path.dirname(__file__))  # 脚本所在目录： d:\Study\30-Days-of-Python-ssy\30-Days-Of-Python\12_Day_Modules

import sys
print(sys.version)

from statistics import * # importing all the statistics modules
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~21.1
print(median(ages))     # 22
print(mode(ages))       # 20
print(stdev(ages))      # ~6.1

lst = [1, 2, 3, 4, 5]
print(mean(lst))
print(median(lst))
print(mode(lst))
print(stdev(lst))

import math
print(math.pi)           # 3.141592653589793, pi constant
print(math.sqrt(2))      # 1.4142135623730951, square root
print(math.pow(2, 3))    # 8.0, exponential function
print(math.floor(9.81))  # 9, rounding to the lowest
print(math.ceil(9.81))   # 10, rounding to the highest
print(math.log10(100))   # 2, logarithm with 10 as base