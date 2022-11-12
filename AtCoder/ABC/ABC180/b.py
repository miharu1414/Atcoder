n = int(input())
a = list(map(int,input().split()))
ans1 = abs(a[0])
ans2 = a[0]**2
ans3 = abs(a[0])
for i in range(1,n):
    ans1 += abs(a[i])
    ans2 += a[i]**2
    ans3 = max(ans3,abs(a[i]))
print(ans1)
import math
print(math.sqrt(ans2))
print(ans3)