n,q = map(int,input().split())
a = list(map(int,input().split()))

dif = [0]*(n-1)
now_sum= 0

for i in range(n-1):
    dif[i] = a[i+1]-a[i]
    now_sum += abs(dif[i])
L,R,V = [],[],[]

for i in range(q):
    l,r,v = map(int,input().split())
    L.append(l)
    R.append(r)
    V.append(v)
for i in range(q):
    l,r,v = L[i],R[i],V[i]

    if l != 1:
        now_sum -= abs(dif[l-2])
        dif[l-2] = dif[l-2] + v
        now_sum += abs(dif[l-2])
    if r != n:
        now_sum -= abs(dif[r-1])
        dif[r-1] = dif[r-1] -v
        now_sum += abs(dif[r-1])
 
    print(now_sum)
