import sys
sys.setrecursionlimit(10**6)

n = int(input())
a = list(map(int,input().split()))
dp = [[0]*(404) for i in range(404)]
flag = [[0]*(404) for i in range(404)]
dp_weight = [[1<<60]*500 for i in range(500)]
def f(x,y):
    if flag[x][y]:
        return [dp_weight[x][y],dp[x][y] ]
    if x > y :
        return 0
    flag[x][y] = 1
    if x == y:
        dp[x][y] = a[x]
        dp_weight[x][y] = 0
        return [dp_weight[x][y],dp[x][y] ]       
    if x == y-1 :
        dp[x][y] = a[x]+a[y]
        dp_weight[x][y] = a[x]+a[y]
        return [dp_weight[x][y],dp[x][y]]
    else:
        for i in range(x,y):
            left = f(x,i)
            right = f(i+1,y)
            if dp_weight[x][y] > left[0] +right[0] + left[1] + right[1]:
                dp_weight[x][y] = left[0] +right[0] + left[1] + right[1]
                dp[x][y] = left[1] + right[1]       
    

    return [dp_weight[x][y],dp[x][y]]  
print(f(0,n-1)[0])

    