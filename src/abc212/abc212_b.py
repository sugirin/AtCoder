"""
https://atcoder.jp/contests/abc212/tasks/abc212_b
"""
X = list(map(int, input()))

cond1 = len(set(X)) == 1
def cond2(X):
    for i in (1,2,3):
        if (X[i-1]+1)%10 != X[i]:
            return False
    return True


if cond1 or cond2(X):
    print('Weak')
else:
    print('Strong')