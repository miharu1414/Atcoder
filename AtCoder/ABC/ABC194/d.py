n = int(input())

from math import factorial
ans = 0
for i in range(1,n):
    ans += n/i
print(ans)