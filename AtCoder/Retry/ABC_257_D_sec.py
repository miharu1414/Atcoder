n = int(input())
x,y,p = [],[],[]
for i in range(n):
    X,Y,P = map(int,input().split())
    x.append(X)
    y.append(Y)
    p.append(P)

dist = [[0]*n for i in range(n)]

for i in range(n):
    for j in range(n):
        dist[i][j] = (abs(x[i]-x[j]) + abs(y[i]-y[j])+p[i]-1)//p[i]

# ワーシャルフロイド法
for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j],max(dist[i][k],dist[k][j]))

# 答えを求める
ans = 10**12
for i in range(n):
    # 始点をi
    kouho = 0
    for j in range(n):
        kouho = max(kouho,dist[i][j])
    ans = min(ans,kouho)
print(int(ans)) 