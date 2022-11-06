n,m = map(int,input().split())
ab = [map(int,input().split()) for i in range(m)]
a,b = [list(i) for i in zip(*ab)]

city = [[] for i in range(n+1)]
num = [0]*(n+1)
for i in range(m):
    city[a[i]].append(b[i])
    city[b[i]].append(a[i])
    num[a[i]]+=1
    num[b[i]]+=1

for i in range(1,n+1):
    ans = sorted(city[i])
    print(num[i],*ans)
    