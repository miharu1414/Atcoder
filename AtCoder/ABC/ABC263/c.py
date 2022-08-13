n,m = map(int,input().split())

import itertools
l = [i for i in range(1,m+1)]

ans = []
for v in itertools.combinations(l, n):
    ans.append(v)
ans.sort()
for i in range(len(ans)):
    print(*ans[i])