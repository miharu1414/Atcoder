import sys
sys.setrecursionlimit(10 ** 6)
n = int(input())
memo = dict()

def rec(x):
    if x == 0:
        return 1
    if x in memo:
        return memo[x]
    else:
        memo[x] = rec(x//2) + rec(x//3)
        return memo[x]
print(rec(n))