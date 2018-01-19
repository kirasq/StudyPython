#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/19 18:16
# @Author  : Kira
# @Email   : kira-qing.sun@cn-bi.com
# @File    : StudyBase.py
# @Software: PyCharm
age = 40
if age<30:
    print 'you age is',age
    print 'sun'
else:
    print 'you age is ',age
# 循环
sun = 0
for x in [1,2,3,4,5]:
    sun += x
print sun

# range 函数，可以快速生成整数序列
print range(1)
print range(10)
print range(1,2)
print range(100,999,2) #range参数的变化

# While循环
sum = 0
n = 99
while n>0:
    sum+=n
    n = n-2
print sum

# Console输入
brith = raw_input('生日是:')
if brith<2000:
    print '00前'
else:
    print '00后'

# 数据类型转换
print '1' < 2
print 1<2
print int('1')<2
print '查看三种结果'

