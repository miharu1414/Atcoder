n,x = map(int,input().split())

a = []
b = []
sum = [0] * (n+1)
for i in range(n):
    X,Y = map(int,input().split())
    a.append(X)
    b.append(Y)

for i in range(n):
    if i == 0:
        sum[i] = a[i]+b[i]
    else:
        sum[i] = a[i]+b[i] + sum[i-1]
ans = 10**20
minb = 10**9
for i in range(n):
    if i >=x:
        break
    if x - i - 1<0:
        break
    minb = min(minb,b[i])
    ans = min(ans,sum[i]+(x-i-1)*minb)
print(int(ans))