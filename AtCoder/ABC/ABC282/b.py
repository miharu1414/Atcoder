n,m = map(int,input().split())
s = [input() for i in range(n)]

ans = 0
for i in range(n-1):
    
    for j in range(i+1,n):
        ok = 1
        for k in range(m):
            if s[i][k] =='x' and s[j][k]=='x':
                ok = 0
        if ok:
            ans +=1
print(ans)