"""
https://atcoder.jp/contests/abc212/tasks/abc212_d
"""
from collections import defaultdict as ddict
Q = int(input())
box = []
xappend = box.append
bias = []
bappend = bias.append
for _ in range(Q):
    query = input()
    if query[0]=='1':
        q, x = map(int, query.split())
        xappend(x)
    elif query[0]=='2':
        q, x = map(int, query.split())
        bappend((len(box),x))
    else: # query[0]=='3'
        for i, b in reversed(bias):
            for j in range(i):
                box[j] += b
        bias = []
        bappend = bias.append
        idx = box.index(min(box))
        print(box[idx])
        box[idx] = 10**10