import sys
sys.setrecursionlimit(10**6)

# 頂点 v を始点とした深さ優先探索
def dfs(v, G, seen, prev):
    seen[v] = True
    # G[v] に含まれる頂点 v2 について、
    for v2 in G[v]:
        # v2 がすでに探索済みならば、スキップする
        if seen[v2]:
            continue
        # そうでなければ、prev[v2] を登録したうえで、頂点 v2 始点で深さ優先探索を行う
        prev[v2] = v
        dfs(v2, G, seen, prev)
    return

# main
# 入力を受け取る
N, s, t = map(int, input().split())
s-=1
t-=1
G = [[] for _ in range(N)]  # グラフを表現する隣接リスト
for i in range(N-1):
    a, b = map(int, input().split())
    a-=1
    b-=1
    # 頂点 a から頂点 b への辺を張る
    G[a].append(b)
    G[b].append(a)

prev = [-1 for _ in range(N)]   # prev[v]：深さ優先探索の際、頂点 v の前にどの頂点を見ていたか
seen = [False for _ in range(N)]    # seen[v]：頂点 v が黒色に塗られているか (探索済みか)
# 頂点 s を始点として深さ優先探索を行う
dfs(s, G, seen, prev)

order = []  # s-t パスを保存する配列
# 頂点 t を開始点として prev をさかのぼることで、s-t パスを求める
now = t
while now != -1:
    order.append(now)
    now = prev[now]
# 配列 order を反転させる
order.reverse()
for i in range(len(order)):
    order[i] += 1

print(*order)