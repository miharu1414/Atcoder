n, m = map(int,input().split())
ab = [map(int,input().split()) for i in range(m)]
a,b = [list(i) for i in zip(*ab)]
G = [[] for i in range(n)]
for i in range(m):
    A, B = a[i]-1,b[i]-1

    # 頂点 A から頂点 B への辺を張る
    G[A].append(B)
    G[B].append(A)

# 各頂点が何手目に探索されたか
# -1 は「まだ探索されていない」ことを表す
dist = [-1] * n

# k 手目に探索された頂点集合を格納 (最大でも N-1 手まで)
nodes = [[] for i in range(n)]

# 頂点 0 を始点とする
dist[0] = 0
nodes[0] = [0]
ans = [0]*n
ans[0] = -1
# k 手目の探索をする
for k in range(1, n):
    # k-1 手目に探索された各頂点 v に対して
    for v in nodes[k - 1]:
        # 頂点 v から 1 手で行ける頂点 next_v を探索
        for next_v in G[v]:
            # 頂点 next_v が探索済みであれば何もしない
            if dist[next_v] != -1:
                continue

            # 頂点 next_v を探索する
            dist[next_v] = dist[v] + 1
            ans[next_v] = v + 1
            nodes[k].append(next_v)

# k = 0, 1, ..., N-1 手目に探索された頂点を出力
if 0 in ans:
    print("No")
else:
    print("Yes")
    for i in range(1,n):
        print(ans[i])
