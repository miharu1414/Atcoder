n,m,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

sum_a = [0]*(n+1)
sum_b = [0]*(m+1)

for i in range(n):
    sum_a[i+1] = sum_a[i] + a[i]
for i in range(m):
    sum_b[i+1] = sum_b[i] + b[i]


ans = 0

import bisect
for i in range(n+1):
    now1 = sum_a[i]
    j = bisect.bisect_right(sum_b,k-now1) -1
    if j>len(sum_b)-1 or now1 + sum_b[j]<=k:
        ans = max(ans,j+i)
print(ans)
    
    