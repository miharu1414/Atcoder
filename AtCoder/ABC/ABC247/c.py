# スタックオーバーフローを防ぐ
import sys
sys.setrecursionlimit(10 ** 6)
n= int(input())

def S(n):
    if n == 1:
        print(1, end=' ')
    else:
        S(n-1)
        print(n,end=' ')
        S(n-1)
S(n)