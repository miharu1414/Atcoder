k, n = map(int,input().split())
a = list(map(int,input().split()))

ruiseki = [0]*(2*n+1)
ruiseki[1] = a[0]
for i in range(1,n):
    ruiseki[i+1] = ruiseki[i] + a[i] - a[i-1]
ruiseki[n+1] = ruiseki[n] + (k-a[n-1]) + a[0]
for i in range(1,n):
    ruiseki[n+i+1] = ruiseki[n+i] + a[i] - a[i-1]

ans = 10**18
for i in range(1,n+1):
    ans = min(ans,ruiseki[i+n-1] - ruiseki[i])
print(ans)