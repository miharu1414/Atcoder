# グラフが無向グラフであるならば　d_ij + d_jk <=> d_ij + d_ky

import heapq

def dijkstra(start, edges, num_node):
    """ 経路の表現
            [終点, 辺の値]
            A, B, C, D, ... → 0, 1, 2, ...とする """
    dist = [float('inf')] * num_node    #スタート地点以外の値は∞で初期化
    dist[start] = 0     #スタートは0で初期化

    node_name = []
    heapq.heappush(node_name, [0, start])

    while len(node_name) > 0:
        #ヒープから取り出し
        _, min_point = heapq.heappop(node_name)
        
        #経路の要素を各変数に格納することで，視覚的に見やすくする
        for factor in edges[min_point]:
            goal = factor[0]   #終点
            cost  = factor[1]   #コスト

            #更新条件
            if dist[min_point] + cost < dist[goal]:
                dist[goal] = dist[min_point] + cost     #更新
                #ヒープに登録
                heapq.heappush(node_name, [dist[min_point] + cost, goal])

    return dist


n, m = map(int,input().split())
abc = [map(int,input().split()) for i in range(m)]
a,b,c = [list(i) for i in zip(*abc)]

Graph = [[] for i in range(n)]
for i in range(m):
    Graph[a[i]-1].append([b[i]-1,c[i]])
    Graph[b[i]-1].append([a[i]-1,c[i]])

d_ik = dijkstra(0,Graph,n)
d_nk = dijkstra(n-1,Graph,n)
for i in range(n):
    print(d_ik[i]+d_nk[i])