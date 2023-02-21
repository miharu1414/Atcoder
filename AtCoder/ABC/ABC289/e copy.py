t = int(input())

def col(array,i):
    if array[i] == 0:
        return 0
    return 1    
from collections import deque


from collections import deque
for _ in range(t):
    def bfs(n, m, u, v, c):
        g = [[] for _ in range(n)]
        for i in range(m):
            g[u[i]-1].append(v[i]-1)
            g[v[i]-1].append(u[i]-1)

        q = deque([(0, n-1, 0)])
        seen = set()

        while q:
            x, y, d = q.popleft()
            if (x, y) in seen:
                continue
            seen.add((x, y))

            if x == y:
                return d

            for a in g[x]:
                if c[a] == c[y]:
                    continue
                q.append((a, y, d + 1))

            for b in g[y]:
                if c[b] == c[x]:
                    continue
                q.append((x, b, d + 1))

        return -1

    n, m = map(int, input().split())
    u = [0] * m
    v = [0] * m
    c = list(map(int,input().split()))

    for i in range(m):
        u[i], v[i] = map(int, input().split())
        u[i]-=1
        v[i]-=1

    print(bfs(n, m, u, v, c))