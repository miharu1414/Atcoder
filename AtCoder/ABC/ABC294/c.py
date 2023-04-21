n, m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

c = a.copy() + b.copy()
c.sort()

import bisect 
ans = []
for i in range(n):
    ans.append(bisect.bisect_right(c,a[i]))
print(*ans)
ans = []
for i in range(m):
    ans.append(bisect.bisect_right(c,b[i]))
print(*ans)
