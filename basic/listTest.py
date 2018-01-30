#!usr/bin/python/
# -*- coding: utf-8 -*-

#list列表
classmates = ["aa","bb","cc"]
print(len(classmates))
print(classmates[-1])

#tuple元祖 区别 tuple一旦初始化就不能修改
classmatess = ("aa","bb","cc")
print(classmatess)
print(classmatess[1])

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0])
print(L[1][1])
print(L[2][2])

#循环
sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum = sum + x
print(sum)

print(list(range(5)))

n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n = n + 1
print("end")

#dict & set
#Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
#相当于Map
d = {"aa" : 20 , "bb" : 30 ,"cc" : 35}
print(d["bb"])
d.pop("aa")
print(d)

#set是一组key的集合，不能重复