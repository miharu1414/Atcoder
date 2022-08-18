from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

n,m,e = map(int,input().split())
G = [[] for i in range(n+m+1)]
densen = []
for i in range(e):
    u,v = map(int,input().split())

    densen.append([u-1,v-1])
    

q = int(input())

uf = UnionFind(n+m)
# 発電所を全連結
for i in range(n,n+m-1):
    uf.union(i,i+1)


que_set = dict()
x = []
for i in range(q):
    X = int(input()) - 1
    que_set[X] = 1
    x.append(X)
for i in range(e):
    if i not in que_set:
        u,v = densen[i]
        uf.union(u,v)
ans = []

now = uf.size(n) - m
for i in range(q):
    ans.append(now)

    u,v = densen[x[q-i-1]]

    uf.union(u,v)
    now = uf.size(n) - m


ans.reverse()
for i in range(q):
    print(ans[i])