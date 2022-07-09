n,x = map(int,input().split())
aa = [list(map(int,input().split())) for i in range(n)]
a = []
for i in range(n):
    a_l = aa[i][1:]
    a.append(a_l)

ans = 0

def dfs(pos , seki):
    global ans
    if pos == n:
        if seki == x:
            ans +=1
        return
    
    for c in a[pos]:
        if seki>x//c:
            continue
        else:
            dfs(pos+1,seki*c)
dfs(0,1)
print(ans)


        
