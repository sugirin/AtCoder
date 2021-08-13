"""
https://atcoder.jp/contests/abc213/tasks/abc213_d
"""
from collections import defaultdict as ddict
from collections import deque
import heapq
N = int(input())
childlen = [[] for _ in range(N+1)]
for _ in range(N-1):
    A, B = map(int, input().split())
    childlen[A].append(-1*B)
    childlen[B].append(-1*A)
for i in range(N+1):
    heapq.heapify(childlen[i])

visited = [False for _ in range(N+1)]
visited[1] = True
route = []
q = deque()
q.append(1)
while len(q) > 0:
    curr = q.pop()
    route.append(curr)
    child = childlen[curr]
    while len(child)>0:
        c = heapq.heappop(child)
        if visited[-1*c]:
            continue
        q.append(curr)
        q.append(-1*c)
        visited[-1*c] = True

print(*route)