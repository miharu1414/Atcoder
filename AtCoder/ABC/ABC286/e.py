n = int(input())
a = list(map(int,input().split()))
s = [input() for i in range(n)]
q = int(input())
uv = [map(int,input().split()) for i in range(q)]
u,v = [list(i) for i in zip(*uv)]


def warshall_floyd(d):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][j] >d[i][k]+d[k][j]:
                    d[i][j]= d[i][k]+d[k][j]
                    score[i][j] = score[i][k] + score[k][j]
                if d[i][j] == d[i][k]+d[k][j] and score[i][j] < score[i][k] + score[k][j]:
                    score[i][j] = score[i][k] + score[k][j]
    return d


# 隣接行列の定義、初期化
# ①コスト(存在しないときはinf)
d = [[float("inf") for i in range(n)] for i in range(n)]
score = [[-1 for i in range(n)] for i in range(n)]
# ②自分自身へのコストは０
for i in range(n):
    d[i][i] = 0

# コスト入力（何もないときは１，問題によっては入力時に指定される）
cost = 1
for i in range(n):
    for j in range(len(s[i])):
        if s[i][j] == 'Y':
            d[i][j] = cost
            score[i][j] = a[j]


# output
warshall_floyd(d)
for i in range(q):
    if d[u[i]-1][v[i]-1] ==float("inf") : print("Impossible")
    else: print(d[u[i]-1][v[i]-1],a[u[i]-1]+score[u[i]-1][v[i]-1])