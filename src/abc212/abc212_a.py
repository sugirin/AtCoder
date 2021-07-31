"""
https://atcoder.jp/contests/abc212/tasks/abc212_a
"""
A, B = map(int, input().split())

if A>0 and B==0:
    print('Gold')
elif A==0 and B>0:
    print('Silver')
else:
    print('Alloy')