"""
https://atcoder.jp/contests/abc215/tasks/abc215_c
"""
S, K = input().split()
K = int(K)
S = list(S)

from itertools import permutations as perm
P = sorted(list(set(perm(S))))
print(''.join(P[K-1]))