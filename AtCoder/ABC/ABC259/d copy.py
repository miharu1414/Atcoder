import math
def d(x,y,x1,y1):
    return ((x-x1)**2+(y-y1)**2)

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


n = int(input())
sx,sy,tx,ty = map(int,input().split())
xyr = [map(int,input().split()) for i in range(n)]
x,y,r = [list(i) for i in zip(*xyr)]



uf = UnionFind(n)

for i in range(n):
    for j in range(i+1,n):
        
        if (r[i]-r[j])**2<d(x[i],y[i],x[j],y[j]) and d(x[i],y[i],x[j],y[j]) < (r[i]+r[j])**2:
            uf.unite(i,j)
        elif d(x[i],y[i],x[j],y[j]) == (r[i]-r[j])**2:
            uf.unite(i,j)
        elif d(x[i],y[i],x[j],y[j]) == (r[i]+r[j])**2:
            uf.unite(i,j)

#sの円を求める
sx_node = []
tx_node = []
for i in range(n):
    if (x[i]-sx)**2 + (y[i]-sy)**2 == r[i]**2:
        sx_node.append(i)
    if (x[i]-tx)**2 + (y[i]-ty)**2 == r[i]**2:
        tx_node.append(i)

for ns in sx_node:
    for nt in tx_node:
        if  uf.same(ns,nt):
            print("Yes")
            exit()
print("No")



