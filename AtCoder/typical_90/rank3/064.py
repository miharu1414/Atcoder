# https://atcoder.jp/contests/typical90/submissions/me

n,q = map(int,input().split())
a = list(map(int,input().split()))
l =[]
r = []
v = []
for i in range(q):
    A,b,c = map(int,input().split())
    l.append(A)
    r.append(b)
    v.append(c)

dif = [0]*(n-1)
for i in range(n-1):
    dif[i] = a[i+1] - a[i]

sum_dif = 0
for i in range(n-1):
    sum_dif += abs(dif[i])

for i in range(q):
    if l[i]==1:
        mae = 0
    else:
        origin_l = dif[l[i]-2]
        dif[l[i]-2] = dif[l[i]-2] + v[i]
        sum_dif -= abs(origin_l)
        mae = abs(dif[l[i]-2])

    if r[i]==n:
        usiro = 0
    else:
        origin_r = dif[r[i]-1]
        dif[r[i]-1] = dif[r[i]-1] - v[i]
        sum_dif-=abs(origin_r)
        usiro = abs(dif[r[i]-1])
    
    
    

    sum_dif += mae + usiro
    print(sum_dif)