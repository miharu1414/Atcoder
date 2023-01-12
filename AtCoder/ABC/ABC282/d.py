import sys
sys.setrecursionlimit(10**6)

n, m = map(int,input().split())
G = [[] for i in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    
    G[a-1].append(b-1)
    G[b-1].append(a-1)


color = [0]*(n)

def dfs(v,p,c):
    ret = [0,0]
    color[v] = c
    if(c==1): ret[0]+=1
    else: ret[1]+=1
    for u in G[v]:
        if u == p or color[u] == -c: continue
        if color[u] == c: return [-1,-1]
        res = dfs(u,v,-c)
        if res[0] == -1:    return [-1,-1]
        ret[0] += res[0]
        ret[1] += res[1]
    return ret

ans = n*(n-1)//2 - m
for i in range(n):
    if color[i]==0:
        res = dfs(i,-1,1)
        if res[0] == -1:
            print(0)
            exit()
    
        ans -= res[0]*(res[0]-1)//2
        ans -= res[1]*(res[1]-1)//2

    
print(ans)                                                                                                                                                              