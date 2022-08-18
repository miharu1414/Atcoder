import sys
sys.setrecursionlimit(10**6)

n,m = map(int,input().split())
G = [[] for i in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)

visited = [-1] * n


def dfs(v):
    

    for next_v in G[v]:
        if visited[next_v] != -1 and visited[next_v] == visited[v]:
            return False
        elif visited[next_v] == -1:
            visited[next_v] = 1 - visited[v]
            if dfs(next_v) == False:
                return False
    return True

flag = 1
for i in range(n):
    
    if visited[i] == -1:
        visited[i] = 0
        if dfs(i) == False:
            flag = 0


            
if flag:
    print("Yes")
else:
    print("No")