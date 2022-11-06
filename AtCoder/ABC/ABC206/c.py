n = int(input())
a = list(map(int,input().split()))

same = len(list(set(a)))

import collections


c = collections.Counter(a)
ans = n*(n-1)//2
for i in c.values():
    ans = ans - i*(i-1)//2
print(ans)