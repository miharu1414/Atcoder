n,q = map(int,input().split())
a = list(map(int,input().split()))
x = [int(input()) for i in range(q)]
a.sort()

import bisect
for i in x:
    jun = bisect.bisect_left(a,i)  
    print(n-jun)
