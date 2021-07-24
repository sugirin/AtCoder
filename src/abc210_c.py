"""
https://atcoder.jp/contests/abc210/tasks/abc210_c
"""

N, K = map(int, input().split())
candies = list(map(int, input().split()))

from collections import deque
from collections import defaultdict as dd
q = deque()
colors = dd(lambda: 0)

max_kinds = 0
for i in range(N):
    current_color = candies[i]
    q.append(current_color)
    colors[current_color] += 1
    if i >= K:
        old_color = q.popleft()
        colors[old_color] -= 1
        if colors[old_color] == 0:
            del colors[old_color]
    max_kinds = max(max_kinds, len(colors))

print(max_kinds)
