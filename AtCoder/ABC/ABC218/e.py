
# スタックオーバーフローを防ぐ
import sys
sys.setrecursionlimit(10 ** 6)
# Union-Find
class UnionFind():
    # 初期化
    def __init__(self, n):
        self.par = [-1] * n
        for i in range(n):
            self.par[i] = i
        self.siz = [1] * n

    # 根を求める
    def root(self, x):
        if self.par[x] == x: return x # x が根の場合は x を返す
        else:
          self.par[x] = self.root(self.par[x]) # 経路圧縮
          return self.par[x]

    # x と y が同じグループに属するか (根が一致するか)
    def issame(self, x, y):
        return self.root(x) == self.root(y)

    # x を含むグループと y を含むグループを併合する
    def unite(self, x, y):
        # x 側と y 側の根を取得する
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry: return False # すでに同じグループのときは何もしない
        # union by size
        if self.siz[rx] > self.siz[ry]: # ry 側の siz が小さくなるようにする
            rx, ry = ry, rx
        self.par[ry] = rx # ry を rx の子とする
        self.siz[rx] += self.siz[ry] # rx 側の siz を調整する
        return True
    
    # x を含む根付き木のサイズを求める
    def size(self, x):
        return self.siz[self.root(x)]


# main
# 入力を受け取る
N, M = map(int, input().split())
graph_edges = [[] for _ in range(M)]    # graph_edges[i]：i 番目の辺情報

left = 0

for i in range(M):
    u, v, w = map(int, input().split())
    w = max(0,w)
    graph_edges[i] = [w,u-1, v-1]
    left += w

# 辺情報を重みの昇順にソートする
graph_edges.sort()
# 要素数 N の Union-Find を用意する
uf = UnionFind(N+1)

ans = 0 # 答えとなる変数
for i in range(M):
    # 重みが i 番目に小さい辺は、頂点 u, v を結ぶ、重み w の辺であるとする
    u, v, w = graph_edges[i][1], graph_edges[i][2], graph_edges[i][0]

    # 頂点 u, v がすでに同じグループに属するなら、この辺は採用しない
    if uf.issame(u, v): 
        ans += w
        continue
    # そうでないなら、この辺を採用する
    # Union-Find 上で u, v を統合して、答えに w を足す
    uf.unite(u, v)

# 答えを出力する
print(ans)