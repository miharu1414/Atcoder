n,k = map(int,input().split())
a = list(map(int,input().split()))

ans = []
for i in range(k,n):
    ans.append(a[i])
for i in range(min(n,k)):
    ans.append(0)
print(*ans)