n = int(input())
ab = [map(int,input().split()) for i in range(n)]
a,b = [list(i) for i in zip(*ab)]

imos = []
for i in range(n):
    imos.append([a[i],1])
    imos.append([b[i]+1,-1])

ans = [0]*(n+1)
num = 0
imos.sort()


before = 0
i = 0
num = 0
while i < 2*n:
    while i<2*n-1 and imos[i][0] == imos[i+1][0]:
        if imos[i][1] == 1:
            num+=1
        else:
            num-=1
        i+=1

    ans[num] += imos[i][0] - before
    if i == 2*n-1:
        break
    before = imos[i][0]
    i+=1
print(ans)