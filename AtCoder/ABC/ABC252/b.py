n,w = map(int,input().split())
a = list(map(int,input().split()))

ans = [0]*1000001
for i in range(n):
    if a[i]<=w:
        ans[a[i]] =1
    for j in range(n):
        if i == j:
            continue
        if a[i]+a[j]<=w:
            ans[a[i]+a[j]]=1
        for k in range(n):
            if i == k or j == k:
                continue
            if a[i]+a[j]+a[k]<=w:
                ans[a[i]+a[j]+a[k]]=1

print(sum(ans))