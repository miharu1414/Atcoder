import sys
sys.setrecursionlimit(10**6)

n,m,k = map(int,input().split())
uva = [map(int,input().split()) for i in range(m)]
if k!=0:
    s = list(map(int,input().split()))
    switch = set(s)
else:
    switch = [-1]

u,v,a = [list(i) for i in zip(*uva)]
G0 = [[] for i in range(200001)]
G1 = [[] for i in range(200001)]
for i in range(m):
    if a[i] == 0:
        G0[u[i]].append(v[i])
        G0[v[i]].append(u[i])
    else:
        G1[u[i]].append(v[i])
        G1[v[i]].append(u[i])        
# 頂点 v を始点とした深さ優先探索

dist = [0]*(200001)
ANS = []
def rec(v,  seen, now,before):
    # 頂点 v を黒く塗る (= seen[v] を true に変える)
    seen[v][now] = True
    if v == n:
        ANS.append(before)
    if v in switch:
        now = abs(now-1)
        seen[v][now] = True
        
    # v を出力する (改行を防ぐため、end 引数を使って命令している)
    # G[v] に含まれる頂点 v2 について、
    if now == 0:
        for v2 in G0[v]:
            # v2 がすでに黒く塗られているならば、スキップする
            if seen[v2][now]: continue
            dist[v2] = dist[v] + 1
            # v2 始点で深さ優先探索を行う (関数を再帰させる)
            rec(v2, seen,now,before+1)
    else:
        for v2 in G1[v]:
            # v2 がすでに黒く塗られているならば、スキップする
            if seen[v2][now]: continue
            # v2 始点で深さ優先探索を行う (関数を再帰させる)
            dist[v2] = dist[v] + 1
            rec(v2, seen,now,before+1)        
    return

# main
now = 1

seen = [[0,0] for i in range(200001)]    # seen[v]：頂点 v が黒く塗られいているなら true, そうでないなら false
# 頂点 0 を始点として深さ優先探索を開始する
rec(1,  seen, now,0)
if len(ANS) == 0:
    print(-1)
else:
    print(min(ANS))