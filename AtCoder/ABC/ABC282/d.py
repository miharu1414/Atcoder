import sys
sys.setrecursionlimit(10**6)


# 頂点 v を始点とした深さ優先探索
def dfs(v, G, color):
    # G[v] に含まれる頂点 v2 について、
    for v2 in G[v]:
        # v2 がすでに探索済みならば、スキップする
        if color[v2] != -1:
            # 隣り合う頂点どうしが同じ色なら、答えは No
            if color[v2] == color[v]: return False
            continue
        # そうでなければ、頂点 v2 の色を color[v] と逆にしたうえで
        # v2 始点で深さ優先探索を行う (関数を再帰させる)
        color[v2] = 1 - color[v]
        if not dfs(v2, G, color): return False
    return True
from collections import defaultdict

class UnionFind():
    """
    Union Find木クラス

    Attributes
    --------------------
    n : int
        要素数
    root : list
        木の要素数
        0未満であればそのノードが根であり、添字の値が要素数
    rank : list
        木の深さ
    """

    def __init__(self, n):
        """
        Parameters
        ---------------------
        n : int
            要素数
        """
        self.n = n
        self.root = [-1]*(n+1)
        self.rank = [0]*(n+1)

    def find(self, x):
        """
        ノードxの根を見つける

        Parameters
        ---------------------
        x : int
            見つけるノード

        Returns
        ---------------------
        root : int
            根のノード
        """
        if(self.root[x] < 0):
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]

    def unite(self, x, y):
        """
        木の併合

        Parameters
        ---------------------
        x : int
            併合したノード
        y : int
            併合したノード
        """
        x = self.find(x)
        y = self.find(y)

        if(x == y):
            return
        elif(self.rank[x] > self.rank[y]):
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if(self.rank[x] == self.rank[y]):
                self.rank[y] += 1

    def same(self, x, y):
        """
        同じグループに属するか判定

        Parameters
        ---------------------
        x : int
            判定したノード
        y : int
            判定したノード

        Returns
        ---------------------
        ans : bool
            同じグループに属しているか
        """
        return self.find(x) == self.find(y)

    def size(self, x):
        """
        木のサイズを計算

        Parameters
        ---------------------
        x : int
            計算したい木のノード

        Returns
        ---------------------
        size : int
            木のサイズ
        """
        return -self.root[self.find(x)]

    def roots(self):
        """
        根のノードを取得

        Returns
        ---------------------
        roots : list
            根のノード
        """
        return [i for i, x in enumerate(self.root) if x < 0]

    def group_size(self):
        """
        グループ数を取得

        Returns
        ---------------------
        size : int
            グループ数
        """
        return len(self.roots())

    def group_members(self):
        """
        全てのグループごとのノードを取得

        Returns
        ---------------------
        group_members : defaultdict
            根をキーとしたノードのリスト
        """
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members
# main
# 入力を受け取る
N, M = map(int, input().split())
G = [[] for _ in range(N)]  # グラフを表現する隣接リスト
exist_edge = set()
U,V  = [],[]
n = N
bangou = [0]*n
if N == 2 and M == 0:
    print(1)
    exit()
uf = UnionFind(n)    
for i in range(M):
    a, b = map(int, input().split())
    
    a-=1
    b-=1
    U.append(a)
    V.append(b)

    bangou[a]+=1
    bangou[b]+=1
    uf.unite(a,b)
    G[a].append(b)
    G[b].append(a)


if uf.group_size()==2:
    ok = 1
elif uf.group_size() == 3:
    ok = 2
else:
    ok = 3
if ok == 3:
    print(0)
    exit()
from collections import deque
if ok == 1:
    dist = [-1] * (n)
    dist[0] = 0
    dist[1] = 0

    d = deque()
    d.append(1)
    color = [0]*n
    color[0] = 0
    que = deque([0])#始点を追加
    bipartite = True
    G = defaultdict(set)
    for i in range(M):
        G[U[i]].add(V[i])
        G[V[i]].add(U[i])
    while len(que):
        p = que.popleft()#直近で追加したグラフの頂点を取得
        for q in list(G[p]):#結合しているグラフの頂点を参照
            if color[q] == 0:#塗られていないなら別の色で塗る
                color[q] = -color[p]
                que.append(q)
            elif color[q] == color[p]:#同じ色だったら2部グラフではないと返し終了させる
                bipartite = False
                break

    if bipartite==False:
        print(0)
        exit()
    a1 = 0
    a2 = 0

    for i in range(len(color)):
        if color[i]%2==0:
            a1 += 1
        else:
            a2 += 1
    tigau = 0

         
    print(a1*a2-M)
    

if ok ==2:
    me= len(uf.group_members())
    color = [0 for i in range(N+1)]
    color[0] = 0
    que = deque([0])#始点を追加
    bipartite = True

    