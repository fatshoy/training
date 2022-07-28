from functools import cache
import sys
@cache
def fib(num):
    if num <= 1:
        return num
    return fib(num-1) + fib(num-2)

sys.setrecursionlimit(10000)
print(fib(10000))