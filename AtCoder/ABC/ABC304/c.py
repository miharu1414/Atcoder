def distance(x1,y1,x2,y2):
    return (x1-x2)**2 + (y1-y2)**2

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

    def unite(self, x, y):
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



n, d = map(int,input().split())
xy = [map(int,input().split()) for i in range(n)]
x,y = [list(i) for i in zip(*xy)]

d2 = d * d

uf = UnionFind(n)  

d = [[] for i in range(n)]
for i in range(n):
    for j in range(i+1,n):
        if distance(x[i],y[i],x[j],y[j]) <= d2:
            uf.unite(i,j)
group = uf.all_group_members()

for k,i in group.items():
    if 0 in i:
        target = set(i)
for i in range(n):
    if i in target:
        print("Yes")
    else:
        print("No")