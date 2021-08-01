"""
https://atcoder.jp/contests/abc212/tasks/abc212_d
"""
import heapq
Q = int(input())
box = []
heapq.heapify(box)
bias = 0
for _ in range(Q):
    query = input()
    if query[0]=='1':
        q, x = map(int, query.split())
        heapq.heappush(box, x - bias)
    elif query[0]=='2':
        q, x = map(int, query.split())
        bias += x
    else: # query[0]=='3'
        x = heapq.heappop(box)
        print(x+bias)
