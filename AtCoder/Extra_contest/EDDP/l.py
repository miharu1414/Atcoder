n = int(input())
a = list(map(int,input().split()))
import sys
sys.setrecursionlimit(10**6)
flag = [[0]*3001 for i in range(3001)]
dp = [[0]*3001 for i in range(3001)]
memo = [[0]*3001 for i in range(3001)]
def f(l,r):
    if(l>r):
        return memo[l][r]
    if flag[l][r]:
        return memo[l][r]

    flag[l][r] = 1
    banme = n - (r-l+1)
    if banme&1:
        res = 1<<60
        res = min(res,f(l+1,r)-a[l])
        res = min(res,f(l,r-1)-a[r])
    else:
        res = -1<<60
        res = max(res,f(l+1,r) + a[l])
        res = max(res,f(l,r-1) + a[r])
    
    memo[l][r] = res
    return res
        
print(f(0,n-1))
