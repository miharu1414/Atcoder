n,m = map(int,input().split())
G = [[] for i in range(n+1)]
for i in range(m):
    x,y = map(int,input().split())
    G[x].append(y)
    G[y].append(x)
q = int(input())
A = []


dist = [-1]*(n+1)

for j in range(q):
    x,k = map(int,input().split())
    nodes = [[]for i in range(k+1)]


    dist[x] = 0

    nodes[0] = [x]
    ans = x

    for z in range(1,k+1):
        for v in nodes[z-1]:
            for next_v  in G[v]:
                if dist[next_v] != -1:
                    continue
                dist[next_v] = dist[v] +1
                nodes[z].append(next_v)

                ans += next_v
    for w in range(k+1):
        for i in nodes[w]:
            dist[i] = -1
    A.append(ans)

for i in A:
    print(i)