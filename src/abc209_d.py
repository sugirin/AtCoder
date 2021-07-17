"""
問題文
高橋王国は N 個の街と N−1 本の道路からなり、街には 1 から N の番号がついています。また、
i(1≤i≤N−1) 本目の道路は街 a_i と街 b_i を双方向に結んでおり、どの街からどの街へもいくつかの道路を通ることで移動できます。道路は全て同じ長さです。

Q 個のクエリが与えられます。i(1≤i≤Q) 番目のクエリでは整数 c_i,d_i が与えられるので、以下の問題を解いてください。

現在高橋君は街 c_i に、青木君は街 d_i にいる。二人が同時に街を出発し、それぞれ街 d_i, c_i を目指して同じ速さで移動するとき、
二人が街で出会うか道路上（両端の街を除く）で出会うかを判定せよ。ただし、二人とも最短経路で移動し、街の中を移動する時間は無視できるものとする。

制約
2≤N≤10**5
1≤Q≤10**5
1≤a_i<b_i≤N (1≤i≤N−1)
1≤c_i<d_i≤N (1≤i≤Q)
入力は全て整数
どの街からどの街へもいくつかの道路を通ることで移動できる

入力
入力は以下の形式で標準入力から与えられる。
N Q
a_1 b_1
a_2 b_2
⋮
a_N−1 b_N−1
c_1 d_1
c_2 d_2
⋮
c_Q d_Q

出力
Q 行出力せよ。 
i(1≤i≤Q) 行目には、i 番目のクエリにおいて二人が街で出会うなら Town、道路上で出会うなら Road と出力せよ。
"""

N, Q = map(int, input().split())
roads = [[] for _ in range(N+1)]
queries = []

for _ in range(N-1):
    a, b = map(int, input().split())
    roads[a].append(b)
    roads[b].append(a)

for _ in range(Q):
    queries.append(tuple(map(int, input().split())))

def distance(c, d):
    ans = 1
    start_points = [c]
    history = [c]
    while True:
        new_start_points = []
        for s in start_points:
            if d in roads[s]:
                return ans
            for dest in roads[s]:
                if dest in history:
                    continue
                history.append(dest)
                new_start_points.append(dest)
        start_points = new_start_points
        ans += 1


for query in queries:
    if distance(query[0], query[1])%2 == 0:
        print("Town")
    else:
        print("Road")