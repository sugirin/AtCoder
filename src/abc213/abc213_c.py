"""
https://atcoder.jp/contests/abc213/tasks/abc213_c
"""
H, W, N = map(int, input().split())
cards = [tuple(map(int, input().split())) for _ in range(N)]
cards_H = sorted(list(set([c[0] for c in cards])))
cards_W = sorted(list(set([c[1] for c in cards])))
Hmap = {ch:i+1 for i,ch in enumerate(cards_H)}
Wmap = {cw:i+1 for i,cw in enumerate(cards_W)}

for ch, cw in cards:
    print(Hmap[ch], Wmap[cw])