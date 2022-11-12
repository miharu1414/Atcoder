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

n = int(input())
ab = [map(int,input().split()) for i in range(n)]
a,b = [list(i) for i in zip(*ab)]

num = set()
num.add(1)
for i in range(n):
    num.add(a[i])
    num.add(b[i])
num = list(num)
num.sort()

junban = []
jun = dict()
gyakujun = dict()
for i in range(len(num)):
    junban.append([i,num[i]])
    jun[num[i]] = i
    gyakujun[i] = num[i]
uf = UnionFind(len(num)+2)
for i in range(n):
    uf.union(jun[a[i]],jun[b[i]])

ans = 0
for x,y in junban:
    if uf.same(0,jun[y]):
        ans = max(ans,y)
        
print(ans)

