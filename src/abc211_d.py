"""
https://atcoder.jp/contests/abc211/tasks/abc211_d
"""
N, M =map(int, input().split())

roads = [[] for _ in range(N+1)]
for i in range(M):
    A, B = map(int, input().split())
    roads[A].append(B)
    roads[B].append(A)

from collections import deque
queue = deque([1])
patterns = [0 for _ in range(N+1)]
patterns[1] = 1
ts = [None for _ in range(N+1)]
ts[1] = 0
while len(queue) > 0:
    src = queue.popleft()
    for dest in roads[src]:
        if ts[dest] is None:
            ts[dest] = ts[src] + 1
            patterns[dest] += patterns[src]
            patterns[dest] %= 10**9 + 7
            queue.append(dest)
        elif ts[dest] == ts[src]+1:
            patterns[dest] += patterns[src]
            patterns[dest] %= 10**9 + 7

print(patterns[-1])