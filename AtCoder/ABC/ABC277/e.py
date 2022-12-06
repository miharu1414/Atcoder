

import heapq

def dijkstra(edges, num_node):
    """ 経路の表現
            [終点, 辺の値]
            A, B, C, D, ... → 0, 1, 2, ...とする """
    node = [float('inf')] * num_node    #スタート地点以外の値は∞で初期化
    node[0] = 0     #スタートは0で初期化

    node_name = []
    heapq.heappush(node_name, [0, 0])

    while len(node_name) > 0:
        #ヒープから取り出し
        _, min_point = heapq.heappop(node_name)

        #経路の要素を各変数に格納することで，視覚的に見やすくする
        for factor in edges[min_point]:
            goal = factor[0]   #終点
            cost  = factor[1]   #コスト

            #更新条件
            if node[min_point] + cost < node[goal]:
                node[goal] = node[min_point] + cost     #更新
                #ヒープに登録
                heapq.heappush(node_name, [node[min_point] + cost, goal])

    return node

def main():
    n, m, k = map(int,input().split())
    uva = [map(int,input().split()) for i in range(m)]
    u,v,a = [list(i) for i in zip(*uva)]
    s = list(map(int,input().split()))
    for i in range(m):
        u[i] -= 1
        v[i] -= 1
        

    num_node = 2*n+2
    Edges = [[] for i in range(2*n+2)]
    for i in range(m):
        if a[i]==1:
            Edges[u[i]].append([v[i],1])
            Edges[v[i]].append([u[i],1])
        else:
            Edges[u[i]+n].append([v[i]+n,1])
            Edges[v[i]+n].append([u[i]+n,1])
            

    for i in range(k):
        Edges[s[i]-1].append([s[i]-1+n,0])
        Edges[s[i]-1+n].append([s[i]-1,0])
        
            
    opt_node = dijkstra(Edges, num_node)

    
    result = []
    for i in range(len(opt_node)):
        result.append(opt_node[i])

    if min(result[n-1],result[2*n-1]) != float('inf'):
        print(min(result[n-1],result[2*n-1]))
    else:
        print(-1)
        
    
if __name__ == '__main__':
    main()
