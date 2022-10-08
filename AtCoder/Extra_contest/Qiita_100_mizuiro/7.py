n, m = map(int,input().split())
if m > 0 :
    xy = [map(int,input().split()) for i in range(m)]
    x,y = [list(i) for i in zip(*xy)]


relation = [[0]*n for i in range(n)]
for i in range(m):
    relation[x[i]-1][y[i]-1] = 1
    relation[y[i]-1][x[i]-1] = 1
    
ans = 0
for i in range(2 ** n):
    
    kouho = []
    for j in range(n):  # このループが一番のポイント
        if ((i >> j) & 1):  # 
            kouho.append(j)
    ok = 1
    for i in range(len(kouho)):
        for j in range(i+1,len(kouho)):
            if relation[kouho[i]][kouho[j]] != 1:
                ok = 0
    if ok == 1:
        ans = max(ans,len(kouho))

print(ans)