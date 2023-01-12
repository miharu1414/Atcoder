n, m, q = map(int,input().split())
a,b,c,d = [],[],[],[]
for i in range(q):
    x,y,z,D = map(int,input().split())
    a.append(x)
    b.append(y)
    c.append(z)
    d.append(D)

ans = 0

l = list(range(1,m+1))
import itertools
for v in itertools.combinations_with_replacement(l, n):
    A = v
    score = 0
    for i in range(q):
        if A[a[i]-1] + c[i] == A[b[i]-1]:
            score += d[i]
    ans = max(ans,score)
print(ans)  