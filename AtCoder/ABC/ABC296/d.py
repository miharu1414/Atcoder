import math
n, m= map(int, input().split())

ans = 10**16
sqm = math.sqrt(m)
for i in range(1,int(math.sqrt(m))+3):
    a = i
    b = m//a - 1
    b1 = m//a
    b2 = b1+1
    if b<=n and a<=n and a*b>=m:
        ans = min(ans,a*b)
    if b1<=n and a<=n and a*b1>=m:
        ans = min(ans,a*b1)
    if b2<=n and a<=n and a*b2>=m:
        ans = min(ans,a*b2)
if ans == 10**16:
    print(-1)
else:
    print(ans)    