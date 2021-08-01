"""
https://atcoder.jp/contests/abc212/tasks/abc212_e
"""
from collections import defaultdict as ddict
N, M, K = map(int, input().split())
MOD = 998244353
disabled = []
for _ in range(M):
    U, V = map(int, input().split())
    disabled.append((U, V))

dp = [[0 for j in range(N+1)] for i in range(K+1)]
dp[0][1] = 1
for k in range(1, K+1):
    prev_total = sum(dp[k-1]) % MOD
    for j in range(N):
        n = j+1
        dp[k][n] = (prev_total - dp[k-1][n]) % MOD
    for u, v in disabled:
        dp[k][u] -= (dp[k-1][v])
        dp[k][v] -= (dp[k-1][u])
        dp[k][u] %= MOD
        dp[k][v] %= MOD

print(dp[-1][1]%MOD)