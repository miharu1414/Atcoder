n,m = map(int,input().split())
ab = [map(int,input().split()) for i in range(m)]
a,b = [list(i) for i in zip(*ab)]
k = int(input())
cd = [map(int,input().split()) for i in range(k)]
c,d = [list(i) for i in zip(*cd)]

ab = [[0,0]]*m
umatta = [0]*(n+1)
Ans = 0
for i in range(2**k):
    ans = 0 
    for j in range(k):
        if (i>>j)&1:
            umatta[c[j]]+=1
        else:
            umatta[d[j]]+=1
    
    # チェック
    for l in range(m):
        if umatta[a[l]] and umatta[b[l]]:
            ans += 1
    for l in range(n+1):
        umatta[l] = 0
    Ans = max(ans,Ans)
print(Ans)