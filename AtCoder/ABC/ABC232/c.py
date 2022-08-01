n,m = map(int,input().split())
ab = [map(int,input().split()) for i in range(m)]
if m == 0:
    print("Yes")
    exit()
a,b = [list(i) for i in zip(*ab)]
cd = [map(int,input().split()) for j in range(m)]
c,d = [list(i) for i in zip(*cd)]

G1 = [[0]*(n) for i in range(n)]
G2 = [[0]*(n) for i in range(n)]
for i in range(m):
    G1[a[i]-1][b[i]-1] = 1
    G1[b[i]-1][a[i]-1] = 1  
    G2[c[i]-1][d[i]-1] = 1
    G2[d[i]-1][c[i]-1] = 1

l = [i for i in range(n)]
import itertools
c = itertools.permutations(l, n)

check = 0
for v in c:
    ok = 1
    for i in range(n):
        for j in range(n):
            if G1[i][j] ^ G2[v[i]][v[j]]:
                ok = 0
    if ok:
        check = 1
if check:
    print("Yes")
else:
    print("No")