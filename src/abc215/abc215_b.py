"""
https://atcoder.jp/contests/abc215/tasks/abc215_b
"""
import math

N = int(input())

k = 0
while 2**k <= N:
    k += 1
print(k-1)