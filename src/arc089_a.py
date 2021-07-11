"""
問題文
シカのAtCoDeerくんは二次元平面上で旅行をしようとしています。 AtCoDeerくんの旅行プランでは、時刻 
0 に 点 (0,0) を出発し、 1 以上 N 以下の各 i に対し、時刻 t_i に 点 (x_i,y_i) を訪れる予定です。

AtCoDeerくんが時刻 t に 点 (x,y) にいる時、 時刻 t+1 には 点 (x+1,y), (x−1,y), (x,y+1), (x,y−1) のうちいずれかに存在することができます。
その場にとどまることは出来ないことに注意してください。 AtCoDeerくんの旅行プランが実行可能かどうか判定してください。

制約
1 ≤ N ≤ 10**5
0 ≤ x_i ≤ 10**5
0 ≤ y_i ≤ 10**5
1 ≤ t_i ≤ 10**5
t_i < t_i+1 (1 ≤ i ≤ N−1)
入力は全て整数

入力
入力は以下の形式で標準入力から与えられる。

N
t_1 x_1 y_1
t_2 x_2 y_2
:
t_N x_N y_N

出力
旅行プランが実行可能ならYesを、不可能ならNoを出力してください。
"""

N = int(input())

t, x, y = 0, 0, 0

for i in range(1, N+1):
    ti, xi, yi = map(int, input().split())
    distance = abs(xi-x) + abs(yi-y)
    time_diff = ti - t
    if time_diff < distance:
        print("No")
        exit()
    elif (time_diff - distance) % 2 == 1:
        print("No")
        exit()
    else:
        t, x, y = ti, xi, yi

print("Yes")