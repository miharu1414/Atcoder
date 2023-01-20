import sys
sys.setrecursionlimit(10**6)

def dfs(x,c):
    seen[x] = 1

    if seen[a[x]]:
        return a[x],c+1
    return dfs(a[x],c+1)

n, k = map(int,input().split())
a = list(map(int,input().split()))
for i in range(n): a[i] -= 1

seen  = [0]*n

cycle_start,cost = dfs(0,0)
left = k - cost
if left < 0:
    new = 0
    for i in range(k):
        new = a[new]
    print(new+1)
    exit()

else:
    b = []
    seen  = [0]*n
    def dfs2(x,num):
        b.append(x)
        seen[x] = 1
        if seen[a[x]]:
            return a[x],num+1
        return dfs2(a[x],num+1)
    _,num = dfs2(cycle_start,0)
    print(b[left%num]+1)
    
    