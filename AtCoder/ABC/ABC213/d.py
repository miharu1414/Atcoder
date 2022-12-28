n = int(input())
ab = [map(int,input().split()) for i in range(n-1)]
a,b = [list(i) for i in zip(*ab)]
Edge = []
for i in range(n-1):
    if a[i] > b[i]:
        a[i],b[i] = b[i],a[i]
    a[i] -= 1
    b[i] -= 1
    Edge.append([a[i],b[i]])

Edge.sort()
G = [[] for i in range(n)]

yet=  [i in range(1,n)]

visited = dict()
for i in range(n-1):
    G[a[i]].append(b[i])
    G[b[i]].append(a[i])
for i in range(n):
    G[i].sort()
now = 0

visited = [0]*n
Ans = []

Sum = 0
now = 0 
before = [0]*n
Ans.append(1)
visited[0] = 1
while 1:
    flag = 1
    for nx in G[now]:
        if visited[nx] == 0:

            before[nx] = now
            now = nx
            visited[nx] = 1
            Sum += 1
            flag = 0
            Ans.append(now+1)
            break
        else:
            continue
    if flag and now == 0:
        print(*Ans)
        exit()
    if flag:
        now = before[now]
        Ans.append(now+1)
    
print(*Ans)