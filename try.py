n,m = map(int,input().split())
G = [[] for i in range(n) ]

for i in range(m):
    a,b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)

seen = [-1] * n


def dfs(v):
    for next_v in G[v]:
        if seen[next_v] != -1:
            if seen[v] == seen[next_v]:
                return False
        else:
            seen[next_v] = 1 - seen[v]
            if dfs(next_v) == False:
                return False
    return True


for i in range(n):
    if seen[i] == -1:
        seen[i]=0
        if  dfs(i) == False:
            print("No")
            exit()
print("Yes")
