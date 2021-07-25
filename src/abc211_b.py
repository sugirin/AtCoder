"""
https://atcoder.jp/contests/abc211/tasks/abc211_b
"""

hits = []
for i in range(4):
    hits.append(input())

hits = set(hits)
if len(hits) == 4:
    print('Yes')
else:
    print('No')
