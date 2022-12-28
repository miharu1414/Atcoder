n,m = map(int,input().split())
a = list(map(int,input().split()))

dp = [[-1]*n for i in range(n)]
def dfs(x,y):
    