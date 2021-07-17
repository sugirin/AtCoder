"""
問題文
長さ N の整数列 C が与えられます。以下の条件を全て満たす長さ N の整数列 A の個数を求めてください。

1 ≤ A_i ≤ C_i (1 ≤ i ≤ N)
A_i ≠ A_j (1 ≤ i < j ≤ N)
ただし、答えは非常に大きくなる可能性があるので、
(10**9+7) で割った余りを出力してください。

制約
1≤N≤2×10**5
1≤C_i≤10**9
入力は全て整数

入力
入力は以下の形式で標準入力から与えられる。
N
C_1 C_2 … C_N

出力
条件を全て満たす整数列 A の個数を (10**9+7) で割った余りを出力せよ。
"""

N = int(input())
C_list = list(map(int, input().split()))

C_list = sorted(C_list)

num_pattern = 1

for i in range(N):
    Ci = C_list[i]
    if Ci - i < 0:
        print(0)
        exit()
    num_pattern *= Ci - i
    num_pattern %= 10**9 + 7

print(num_pattern)