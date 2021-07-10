"""
問題文
X 段重ねの鏡餅 (X≥1) とは、X 枚の円形の餅を縦に積み重ねたものであって、どの餅もその真下の餅より直径が小さい（一番下の餅を除く）もののことです。
例えば、直径 10、8、6 センチメートルの餅をこの順に下から積み重ねると 3 段重ねの鏡餅になり、餅を一枚だけ置くと 1 段重ねの鏡餅になります。

ダックスフンドのルンルンは N 枚の円形の餅を持っていて、そのうち i 枚目の餅の直径は d_i センチメートルです。
これらの餅のうち一部または全部を使って鏡餅を作るとき、最大で何段重ねの鏡餅を作ることができるでしょうか。

制約
1≤N≤100
1≤d_i≤100
入力値はすべて整数である。

入力
入力は以下の形式で標準入力から与えられる。

N
d_1
:
d_N

出力
作ることのできる鏡餅の最大の段数を出力せよ。
"""

N = int(input())
ricecakes = []
for _ in range(N):
    ricecakes.append(int(input()))

ricecakes_uniq = list(set(ricecakes))
print(len(ricecakes_uniq))