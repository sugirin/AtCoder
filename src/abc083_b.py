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

def correct_solver(N, A, B):
    total = 0

    for i in range(N+1):
        digits_total = 0
        for digit in str(i):
            digits_total += int(digit)
        if A <= digits_total and digits_total <= B:
            total += i

    return total

def wrong_solver(N, A, B):
    total = 0
    
    for h in range(2):
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
                        total += 1000*i + 100*j + 10*k + l
    
    return total

N, A, B = 1, 1, 36

import random

for N in range(10001):
    for A in range(37):
        for B in range(A, 37):
            if correct_solver(N, A, B) != wrong_solver(N, A, B):
                print(N, A, B, correct_solver(N, A, B), wrong_solver(N, A, B))

