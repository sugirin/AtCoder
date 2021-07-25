"""
https://atcoder.jp/contests/abc211/tasks/abc211_c
"""
S = list(input())

ctoi = {
    'c':0,
    'h':1,
    'o':2,
    'k':3,
    'u':4,
    'd':5,
    'a':6,
    'i':7,
}

patterns = [0 for _ in range(8)]

for c in S:
    if c not in ctoi:
        continue
    if c == 'c':
        patterns[0] += 1
    else:
        patterns[ctoi[c]] += patterns[ctoi[c]-1]
    
    if patterns[ctoi[c]] >= 10**9 + 7:
        patterns[ctoi[c]] -= 10**9 + 7

print(patterns[-1])