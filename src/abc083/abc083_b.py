"""
問題文
1 以上 N 以下の整数のうち、10 進法での各桁の和が A 以上 B 以下であるものの総和を求めてください。

制約
1 ≤ N ≤ 10**4
1 ≤ A ≤ B ≤ 36
入力はすべて整数である

入力
入力は以下の形式で標準入力から与えられる。

N A B

出力
1 以上 N 以下の整数のうち、10 進法での各桁の和が A 以上 B 以下であるものの総和を出力せよ。
"""

N, A, B = map(int, input().split())

total = 0

for h in range(10):
    if h+9+9+9+9 < A or h > B or (10000*h) > N:
        continue
    for i in range(10):
        if h+i+9+9+9 < A or h+i > B or (10000*h + 1000*i) > N:
            continue
        for j in range(10):
            if h+i+j+9+9 < A or h+i+j > B or (10000*h + 1000*i + 100*j) > N:
                continue
            for k in range(10):
                if h+i+j+k+9 < A or h+i+j+k > B or (10000*h + 1000*i + 100*j + 10*k) > N:
                    continue
                for l in range(10):
                    if h+i+j+k+l < A or h+i+j+k+l > B or (10000*h + 1000*i + 100*j + 10*k + l) > N:
                        continue
                    total += 10000*h + 1000*i + 100*j + 10*k + l

print(total)


