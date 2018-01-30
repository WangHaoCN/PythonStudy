#!usr/bin/python/
# -*- coding: utf-8 -*-

def power(x):
    return x * x
print(power(2))

def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

print(fact(5))