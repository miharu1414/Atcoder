n,m = map(int,input().split())
G = [[] for i in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
q = int(input())
dist = [-1]*n
for _ in range(q):
    x,k = map(int,input().split())
    x -= 1

    
    nodes = [[] for i in range(k+1)]
    ans = []
    dist[x] = 0
    nodes[0].append(x)
    ans.append(x+1)
    for i in range(1,k+1):
        for v in nodes[i-1]:
            for next_v in G[v]:
                if dist[next_v]!=-1:
                    continue
                ans.append(next_v+1)
                nodes[i].append(next_v)
                dist[next_v] = dist[v] + 1
    for i in range(len(ans)):
        dist[ans[i]-1] = -1
    print(sum(ans))
    dist[x] = -1