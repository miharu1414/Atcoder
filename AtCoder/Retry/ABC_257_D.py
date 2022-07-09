n = int(input())
INF = 10**12
x,y,p = [],[],[]
for i in range(n):
    a,b,c = map(int,input().split())
    x.append(a)
    y.append(b)
    p.append(c)


dist =[[0]*n for i in range(n)]

# 初期の重みを計算
for i in range(n):
    for j in range(n):
        dist[i][j] = (abs(x[i]-x[j])+abs(y[i]-y[j])+p[i]-1)//p[i]


# ワ―シャルフロイド法
for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j],max(dist[i][k],dist[k][j]))

ans = INF
for i in range(n):
    max_cost = -1
    for j in range(n):
        max_cost = max(max_cost,dist[i][j])
    ans = min(ans,max_cost)
print(int(ans))