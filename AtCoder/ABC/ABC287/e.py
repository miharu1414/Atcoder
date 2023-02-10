n = int(input())
s = [input() for i in range(n)]

# LCP配列の構築
# ここでTは文字列、SAはTのSuffix Array

from collections import defaultdict
d = dict()
for i in range(n):
    d[s[i]] = i
t = s.copy()
t.sort()
lcp = [0]*(n-1)
for i in range(n-1):
    lcp1 = 0
    while( lcp1 < len(t[i]) and lcp1 < len(t[i+1]) and t[i][ lcp1] == t[i+1][lcp1]):
        lcp1+=1
    lcp[i]  = lcp1

import bisect
for i in range(n):
    now = s[i]
    idx = bisect.bisect_left(t,s[i])
    if idx == 0:
        print(lcp[idx])
    elif idx == n-1:
        print(lcp[idx-1])
    else:
        print(max(lcp[idx-1],lcp[idx]))
        