l, n1, n2 = map(int,input().split())
v1, l1 = [],[]
v2, l2 = [],[]
for i in range(n1):
    a,b = map(int,input().split())
    v1.append(a)
    l1.append(b)
    
for i in range(n2):
    a,b = map(int,input().split())
    v2.append(a)
    l2.append(b)

from collections import defaultdict
d = defaultdict(list)


before = -1
for i in range(n1):
    d[v1[i]].append([before + 1, before + l1[i]])
    before += l1[i]

now = -1
ans = 0
for i in range(n2):
    if v2[i] not in d:
        continue
    s = now + 1
    e = now + l2[i]
    now += l2[i]
    for a,b in d[v2[i]]:
        k =  min(b,e) - max(a,s)+1
        kaburi = max(k,0)
        ans += kaburi        
        if k >0:
            break
print(ans)