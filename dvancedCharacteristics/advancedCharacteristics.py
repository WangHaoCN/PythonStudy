#!usr/bin/python/
# -*- coding: utf-8 -*-
#高级特性

from collections import Iterable
import os

#切片
#切片是取一个list或tuple的部分元素是非常常见的操作
L = ['Michael','Sarah','Tracy','Bob','Jack']
print(L[0:3])
print(L[-1])

#迭代
#如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）
d = {'a':1 , 'b':2 , 'c':3}
for key in d:
    print(key)

#判断一个对象是否可以被迭代
print(isinstance([1,2,3], Iterable))
print(isinstance("abc", Iterable))
print(isinstance(1, Iterable))

#列表生成式 range
#列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式
print(list(range(1, 11)))

li = []
for x in range(1,11):
    li.append( x * x )
print(li)

print([x * x for x in range(1, 11) if x % 2 == 0])

#os.listdir 可以列出文件和目录
print([d for d in os.listdir('d:/')])

#生成器
#在python中，一边循环一边计算的机制，称为生成器：generator
g = (x * x for x in range(10))
print(g)

#集合数据类型（list，tuple，dict，set，str）和generator等均称为可迭代对象 Iterable
print(isinstance([],Iterable))
print(isinstance({},Iterable))
print(isinstance('abc',Iterable))
print(isinstance((x for x in range(10)),Iterable))

#可以作用于for循环的对象统称为可迭代对象 Iterable
#可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
print("range创建的对象是否可迭代:",isinstance((x for x in range(10)),Iterable))