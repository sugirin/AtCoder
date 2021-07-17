"""
問題文
高橋辞書には N 個の単語が載っており、i(1≤i≤N) 番目の単語は s_i です。
高橋君と青木君は高橋辞書を使って 3 しりとりをします。 3 しりとりのルールは以下です。

高橋君と青木君は、高橋君から始めて交互に単語を言い合っていく。
各プレーヤーは前の人が言った単語の最後の 3 文字で始まる単語を言わなければならない。
例えば、前の人が Takahashi と言った場合、次の人は ship、shield などを言うことができ、Aoki、sing、his などを言うことはできない。
大文字と小文字は区別される。例えば、Takahashi のあとに ShIp を言うことはできない。
言う単語がなくなった方が負ける。
高橋辞書に載っていない単語を言うことはできない。
同じ単語は何度でも使ってよい。
各 i(1≤i≤N) について、高橋君が 3 しりとりを単語 s_i から始めたときどちらが勝つかを判定してください。
ただし、二人とも最善に行動するとします。具体的には、自分が負けないことを最優先し、その次に相手を負かすことを優先します。

制約
N は 1 以上 2×10**5 以下の整数
s_i は英小文字と英大文字のみからなる長さ 3 以上 8 以下の文字列

入力
入力は以下の形式で標準入力から与えられる。

N
s_1
s_2
⋮
s_N

出力
N 行出力せよ。
i(1≤i≤N) 行目には、高橋君が 3 しりとりを単語 s_i から始めたとき、
高橋君が勝つなら Takahashi、青木君が勝つなら Aoki、しりとりが永遠に続き勝敗が決まらないなら Draw と出力せよ。
"""
from collections import defaultdict as ddict
from collections import deque
N = int(input())
words = [input() for _ in range(N)]


nodes = set()
for w in words:
    nodes.add(w[:3])
    nodes.add(w[-3:])

node_to_id = {node:i for i, node in enumerate(nodes)}
num_nodes = len(nodes)

# i番目のノードからj番目のノードに辺が出ていることを i in edge[j] で表す
# i番目のノードから何本の辺が出ているかを degrees[i] で表す
edge = [[] for j in range(num_nodes)]
degrees = [0 for _ in range(num_nodes)]
for word in words:
    i = node_to_id[word[:3]]
    j = node_to_id[word[-3:]]
    edge[j].append(i)
    degrees[i] += 1

# i番目のノードにいるとき、conditions[i] が1なら勝ち、-1なら負け、0なら引き分け
conditions = [0 for _ in range(num_nodes)]

queue = deque()
for i in range(num_nodes):
    if degrees[i] == 0:
        conditions[i] = -1
        queue.append(i)

# 後退解析を行う
while len(queue) > 0:
    j = queue.popleft()
    for i in edge[j]:
        if conditions[i] != 0:
            continue
        degrees[i] -= 1
        if degrees[i] == 0 and conditions[j] == 1:
            conditions[i] = -1
            queue.append(i)
        elif conditions[j] == -1:
            conditions[i] = 1
            queue.append(i)

# その単語を言った時、遷移先のノードのconditionがどうなっているかで判定する
for word in words:
    j = node_to_id[word[-3:]]
    if conditions[j] == -1:
        print('Takahashi')
    elif conditions[j] == 1:
        print('Aoki')
    else:
        print('Draw')