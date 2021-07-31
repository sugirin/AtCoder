"""
https://atcoder.jp/contests/abc212/tasks/abc212_c
"""
N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))

min_diff = 10**10
i, j = 0, 0
while i<N or j<M:
    if A[i] < B[j]:
        while A[i] < B[j]:
            curr_A = A[i]
            i += 1
            if i==N:
                break
        min_diff = min(min_diff, B[j]-curr_A)
        if i==N:
            break
    elif A[i] > B[j]:
        while A[i] > B[j] and j<M:
            curr_B = B[j]
            j += 1
            if j==M:
                break
        min_diff = min(min_diff, A[i]-curr_B)
        if j==M:
            break
    else:
        min_diff = 0
        break

print(min_diff)
