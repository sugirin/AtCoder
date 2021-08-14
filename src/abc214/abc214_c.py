"""
https://atcoder.jp/contests/abc214/tasks/abc214_c
"""
N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

init_idx = T.index(min(T))

for i in range(N):
    idx = (init_idx + i + N) % N
    nxt = (idx + 1 + N) % N
    T[nxt] = min(T[nxt], T[idx]+S[idx])

print('\n'.join(map(str,T)))
