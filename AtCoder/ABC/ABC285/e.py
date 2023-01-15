n = int(input())
a = list(map(int,input().split()))

import math
A = 0
for i in range(1,n//2+1):
    ans = 0
    for j in range(n):
        syuuki = math.ceil(n / i)
        if j % syuuki == 0:
            continue
        min_d = min(j%syuuki, abs((syuuki - j)%syuuki))
        ans += a[min_d-1]
    A = max(A,ans)
print(A)
            
            
        
        