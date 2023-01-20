n, x, y = map(int,input().split())

G = [[]for i in range(n)]
dis = [0]*n
for i in range(n-1):
    G[i].append(i+1)
    G[i+1].append(i)
G[x-1].append(y-1)
G[y-1].append(x-1)
seen = [0]*n

# -1 は「まだ探索されていない」ことを表す
dist = [-1] * n

# k 手目に探索された頂点集合を格納 (最大でも N-1 手まで)
nodes = [[] for i in range(n)]

# 頂点 0 を始点とする
dist[0] = 0
nodes[0] = [0]

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
            nodes[k].append(next_v)

# k = 0, 1, ..., N-1 手目に探索された頂点を出力


ans = [0 for i in range(n)]
distance = [10**10]*3
for i in range(n):
    for j in range(i+1,n):
        if i == j:
            continue
        
        

        distance[1] = j - i
        distance[2] = abs(dist[i]-dist[x-1]) +1 +abs(dist[j]-dist[y-1])
        ans[min(distance)] += 1
for i in range(1,n):
    print(ans[i])
    