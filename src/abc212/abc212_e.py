"""
https://atcoder.jp/contests/abc212/tasks/abc212_e
"""
from collections import defaultdict as ddict
N, M, K = map(int, input().split())
disabled = ddict(lambda: [])
for _ in range(M):
    U, V = map(int, input().split())
    disabled[U].append(V)
    disabled[V].append(U)

dp = [[0 for j in range(N+1)] for i in range(K+1)]
dp[0][1] = 1
for k in range(1, K+1):
    for j in range(N):
        n = j+1
        dp[k][n] = sum(dp[k-1]) - dp[k-1][n]
        for d in disabled[n]:
            dp[k][n] -= dp[k-1][d]

print(dp[-1][1]%998244353)