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


n, m = map(int,input().split())
a,b,c,d = [],[],[],[]
for i in range(m):
    A,B,C,D = map(str,input().split())
    a.append(int(A)-1)
    b.append(B)
    c.append(int(C)-1)
    d.append(D)
def f(x):
    if x =='R':
        return 0
    else:
        return n
def invf(x):
    if x =='R':
        return n
    else:
        return 0
uf = UnionFind(2*n)
is_linked = [0]*(2*n)
ans2 = 0
for i in range(m):
    
    if is_linked[a[i]+invf(b[i])]:
        uf.union(a[i],a[i]+n)
    if is_linked[c[i]+invf(d[i])]:
        uf.union(c[i],c[i]+n)
    if uf.same(a[i]+f(b[i]),c[i]+f(d[i])):
        ans2 += 1
    if a[i] == c[i]:
        ans2 += 1
    uf.union(a[i]+f(b[i]),c[i]+f(d[i]))
    is_linked[a[i]+f(b[i])] = 1
    is_linked[c[i]+f(d[i])] = 1

for i in range(n):
    uf.union(i,i+n)
ans1 = uf.group_count()
ans1 -= ans2
print(ans2,ans1)