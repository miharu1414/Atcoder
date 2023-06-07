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

n, m = map(int,input().split())
if m > 0:
    uv = [map(int,input().split()) for i in range(m)]
    u,v = [list(i) for i in zip(*uv)]
k = int(input())

xy = [map(int,input().split()) for i in range(k)]
x,y = [list(i) for i in zip(*xy)]

Q = int(input())
pq = [map(int,input().split()) for i in range(Q)]
p,q = [list(i) for i in zip(*pq)]

uf = UnionFind(n+1)
for i in range(m):
    uf.unite(u[i],v[i])

deniedPath = dict()
for i in range(k):
    X = uf.find(x[i])
    Y = uf.find(y[i])
    deniedPath[(min(X,Y),max(X,Y))] = 1

for i in range(Q):
    p_parent = uf.find(p[i])
    q_parent = uf.find(q[i])
    if (min(p_parent,q_parent),max(p_parent,q_parent)) in deniedPath:
        print("No")
    else:
        print("Yes")
    
    
    
    
    