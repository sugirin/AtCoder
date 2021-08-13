"""
https://atcoder.jp/contests/abc213/tasks/abc213_b
"""
N = int(input())
A = list(map(int, input().split()))

max_A = max(A)
max_idx = A.index(max_A)
A[max_idx] = 0

max_A = max(A)
max_idx = A.index(max_A)
print(max_idx+1)
