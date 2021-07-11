"""
問題文
英小文字からなる文字列 S が与えられます。 
Tが空文字列である状態から始め、以下の操作を好きな回数繰り返すことで S=T とすることができるか判定してください。

T の末尾に dream dreamer erase eraser のいずれかを追加する。

制約
1≦|S|≦10**5
S は英小文字からなる。

入力
入力は以下の形式で標準入力から与えられる。

S

出力
S=T とすることができる場合 YES を、そうでない場合 NO を出力せよ。
"""

S = input()

while S != "":
    if S[-5:] == "dream":
        S = S[:-5]
    elif S[-5:] == "erase":
        S = S[:-5]
    elif S[-7:] == "dreamer":
        S = S[:-7]
    elif S[-6:] == "eraser":
        S = S[:-6]
    else:
        break

if S == "":
    print("YES")
else:
    print("NO")