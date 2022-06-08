n = int(input())
a = list(map(int,input().split()))
b  = list(map(int,input().split()))
c = list(map(int,input().split()))

dpa = [0]*47
dpc = [0]*47
dpb = [0]*47
for i in range(n):
    dpa[a[i]%46]+=1
    dpb[b[i]%46]+=1
    dpc[c[i]%46]+=1
ans = 0
for i in range(46):
    for j in range(46):
        for k in range(46):
            if (i + k + j)%46 == 0:
                ans += dpa[i]*dpb[j]*dpc[k]
print(ans)
