"""
問題文
N 枚のカードがあります. i 枚目のカードには, a_i という数が書かれています.
Alice と Bob は, これらのカードを使ってゲームを行います. 
ゲームでは, Alice と Bob が交互に 1 枚ずつカードを取っていきます. 
Alice が先にカードを取ります.
2 人がすべてのカードを取ったときゲームは終了し, 取ったカードの数の合計がその人の得点になります. 
2 人とも自分の得点を最大化するように最適な戦略を取った時, Alice は Bob より何点多く取るか求めてください.

制約
N は 1 以上 100 以下の整数
a_i (1≤i≤N) は 1 以上 100 以下の整数

入力
入力は以下の形式で標準入力から与えられる.

N
a_1 a_2 a_3 ... a_N

出力
両者が最適な戦略を取った時, Alice は Bob より何点多く取るかを出力してください.
"""

N = int(input())
card_nums = list(map(int, input().split()))

card_nums = sorted(card_nums, reverse=True)
alice_points = sum(card_nums[::2])
bob_points = sum(card_nums) - alice_points

print(alice_points - bob_points)