"""
https://atcoder.jp/contests/abc214/tasks/abc214_d
"""
N = int(input())
roads = [[] for i in range(N)]
f_table = [[0 for i in range(N)] for j in range(N)]
for n in range(N-1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    roads[u].append((v, w))
    roads[v].append((u, w))

from collections import deque
q = deque()

for init in range(N-1):
    q.append(init)
    visited = [False for i in range(N)]
    while len(q) > 0:
        node = q.pop()
        visited[node] = True
        for nxt, w in roads[node]:
            if visited[nxt]:
                continue
            q.append(nxt)
            if w > f_table[init][nxt]:
                f_table[init][nxt] = w
                f_table[nxt][init] = w

total = 0
for i in range(N-1):
    for j in range(i+1, N):
        total += f_table[i][j]
print(total)