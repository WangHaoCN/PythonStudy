#高阶函数
from functools import reduce
#函数名实际上就是指向函数的变量

#一个函数可以接受另一个函数作为参数，这种函数称为高阶函数
def add(x,y,f):
    return f(x) + f(y)
print(add(1,-2,abs))

#map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
'''
第一个参数为函数，第二个参数为Iterable，map将每个元素使用函数处理，返回新的Iterable
'''
def fun(x):
    return x * x
aa = map(fun,[1,2,3,4,5,6,7,8,9])
print(aa)
print(list(aa))
L = []
for n in [1,2,3,4,5,6,7,8]:
    L.append(fun(n))
print(list(L))
'''
Reduce有两个参数，一个function，一个Iterater 在function中必须有两个参数，叠加操作
'''
def fun1(x,y):
    return x*10+y
redu = reduce(fun1,[1,2,3,4,5,6,7,8])
print(redu)

'''
filter 用于过滤序列 也接受一个函数一个序列
'''
def is_odd(n):
    return n%2 ==1
filterTest = filter(is_odd,[1,2,3,4,5,6,7,8,9])
print(list(filterTest))

def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty(),[1,2,3,4,5,'','','',6,7,8])))

'''
sorted 排序算法
'''
print(list(sorted([36, 5, -12, 9, -21])))
print(list(sorted([36, 5, -12, 9, -21], key=abs)))
