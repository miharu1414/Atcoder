t = int(input())

def col(array,i):
    if array[i] == 0:
        return 0
    return 1
for _ in range(t):
    n, m = map(int,input().split())
    G = [[] for i in range(n) ]
    c = list(map(int,input().split()))
    uv = [map(int,input().split())for i in range(m)]
    u,v = [list(i) for i in zip(*uv)]
    for i in range(m):
        G[u[i]-1].append(v[i]-1)
        G[v[i]-1].append(u[i]-1)
    
    
    
    color = [0]*n
    for i in range(n):
        if c[i] == 1:
            color[i] = 1
        # -1 は「まだ探索されていない」ことを表す
    dist1 = [-1] * n
    dist2 = [-1] * n
    # k 手目に探索された頂点集合を格納 (最大でも N-1 手まで)
    nodes1 = [[[],[]] for i in range(n)]
    nodes2 = [[[],[]] for i in range(n)]

    # 頂点 0 を始点とする
    dist1[0] = 0
    if col(c,0): nodes1[0][1] = [0]
    else: nodes1[0][0] = [0]
    dist2[n-1] = 0
    if col(c,n-1): nodes2[0][1] = [n-1]
    else: nodes2[0][0] = [n-1]
    # k 手目の探索をする
    for k in range(1, n):
        
        for i in range(2):
        # k-1 手目に探索された各頂点 v に対して
            visit2 = set()
            for v2 in nodes2[k-1][~i]:
                for next_v2 in G[v2]:

                    if dist2[next_v2] != -1:
                        continue

                    # 頂点 next_v を探索する
                    visit2.add(next_v2)
                    dist2[next_v2] = dist2[v2] + 1
                    nodes2[k][color[next_v2]].append(next_v2)
                    
            for v1 in nodes1[k - 1][i]:
                
                # 頂点 v から 1 手で行ける頂点 next_v を探索
                for next_v1 in G[v1]:
                    if next_v1 in visit2:
                        continue
                    # 頂点 next_v が探索済みであれば何もしない
                    if dist1[next_v1] != -1:
                        continue

                    # 頂点 next_v を探索する
                    dist1[next_v1] = dist1[v1] + 1
                    nodes1[k][color[next_v1]].append(next_v1)
   

    if dist1[n-1] != -1 and dist2[0] != -1:
        print(dist1[n-1])                        