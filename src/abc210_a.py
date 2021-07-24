"""

"""

N, A, X, Y = map(int, input().split())

total = N*X
if N>A:
    total += (Y-X)*(N-A)

print(total)