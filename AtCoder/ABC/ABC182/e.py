


h,w,n,m = map(int,input().split())
ab = [map(int,input().split()) for i in range(n)]
a,b = [list(i) for i in zip(*ab)]
cd = [map(int,input().split()) for i in range(m)]
c,d = [list(i) for i in zip(*cd)]

denkyu = [[0]*1501 for i in range(1501)]
block = [[0]*1501 for i in range(1501)]
for i in range(n):
    denkyu[a[i]][b[i]] = 1
for i in range(m):
    block[c[i]][d[i]] = 1

from collections import defaultdict
d1 = []
d2 = []


for i in range(n):
    d1.append([b[i],a[i]])
    d2.append([a[i],b[i]])
    
for i in range(m):
    d1.append([d[i],c[i]])
    d2.append([c[i],d[i]])

d1.sort()
d2.sort()

cnt = 0
import bisect
for i in range(1,h+1):
    for j in range(1,w+1):
        ok = 0
        if block[i][j]:
            continue
        
        else:
            if i != h:
                idx = bisect.bisect_left(d1,[j,i])
                       
                if idx<len(d1) and d1[idx][0] == j and denkyu[d1[idx][1]][d1[idx][0]]:
                    ok = 1
                    cnt += 1
                    break
                    
            if i != 1:
                idx = bisect.bisect_right(d1,[j,i]) -1
            
                if idx<len(d1) and d1[idx][0] == j and denkyu[d1[idx][1]][d1[idx][0]]:
                    ok = 1
                    cnt += 1
                    break
            
            if j != w:
                idx = bisect.bisect_left(d2,[i,j])
                
                if idx<len(d2) and d2[idx][0] == i and denkyu[d2[idx][0]][d2[idx][1]]:
                    ok = 1
                    cnt += 1
                    break
            
            if j != 1:                
                idx = bisect.bisect_right(d2,[i,j]) -1
             
                if idx<len(d2) and d2[idx][0] == i and denkyu[d2[idx][0]][d2[idx][1]]:
                    ok = 1
                    cnt += 1



print(cnt)


