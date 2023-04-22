n,t = map(int,input().split())
c = list(map(int,input().split()))
r  = list(map(int,input().split()))

import collections
d = dict()
atai = dict()
for i in range(n):
    atai[r[i]] = i+1
for i in range(n):
    if c[i] not in d:
        d[c[i]] = r[i]
    else:
        d[c[i]] = max(d[c[i]],r[i])

if t in d:
    print(atai[d[t]])
else:
    print(atai[d[c[0]]])
        
