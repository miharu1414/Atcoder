n, l,r = map(int,input().split())
a = list(map(int,input().split()))

L_min = [0]*(n+1)
for i in range(n):
    L_min[i+1] = min(L_min[i]+a[i],(i+1)*l)
R_min = [0]*(n+1)
for i in range(n-1,-1,-1):
    R_min[i] = min(R_min[i+1]+a[i],(n-i)*r)
ans = 1<<60 
for i in range(n+1):
    ans = min(ans,L_min[i] + R_min[i])
print(ans)