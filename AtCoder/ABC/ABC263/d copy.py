n,l,r = map(int,input().split())
a = list(map(int,input().split()))
 
import copy
a_copy = a.copy()
 
 
dpl= [0] * n
for i in range(n):
    if i ==0:
        dpl[i] = a[i]
    else:
        dpl[i] = dpl[i-1] + a[i]
 
 
left = 0
difl = [0] * (n+1)
d_l = []
d_l.append([0,0])
for i in range(n):
    difl[i+1] = -(dpl[i] - l*(i+1))
    d_l.append([difl[i+1],i+1])
 
 
d_l.sort()
posx = d_l[0][1]
for i in range(posx):
    a[i] = l
 



dpr= [0] * n
for i in range(n):
    if i ==0:
        dpr[i] = a[n-i-1] 
    else:
        dpr[i] = dpr[i-1] + a[n-i-1]
 
difr = [0] * (n+1)
d_r = []
d_r.append([0,0])
 
for i in range(n):
    difr[i+1] = -(dpr[i] - r*(i+1))
    d_r.append([difr[i+1],i+1])
d_r.sort()
posy = d_r[0][1]
for i in range(posy):
    a[n-i-1] = r
 
ans1 = sum(a)
print(ans1)
 
