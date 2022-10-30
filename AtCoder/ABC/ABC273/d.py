h,w,rs,cs = map(int,input().split())
rs-=1
cs-=1

retu = []
gyou = []
n = int(input())

for i in range(n):
    a,b = map(int,input().split())
    a-=1
    b-=1
    retu.append([b,a])
    gyou.append([a,b])
retu.sort()
gyou.sort()
q = int(input())
import bisect
for i in range(q):
    d,l = map(str,input().split())
    l = int(l)
    
    if d=='L':
        possible = bisect.bisect_left(gyou,[rs,cs])
        if possible == 0 or gyou[possible-1][0] != rs:
            cs = max(0,cs-l)
        else:
            cs = max(gyou[possible-1][1]+1,cs-l)
 
    elif d=='R':
        possible = bisect.bisect_left(gyou,[rs,cs])
        if possible == n or gyou[possible][0] != rs:
            cs = min(w-1,cs+l)
        else:
            cs = min(gyou[possible][1]-1,cs+l) 
    
    elif d=='U':
        possible = bisect.bisect_left(retu,[cs,rs])
        if possible == 0 or retu[possible-1][0] != cs:
            rs = max(0,rs-l)
        else:
            rs = max(retu[possible-1][1]+1,rs-l)
    else:
        possible = bisect.bisect_left(retu,[cs,rs])
        if possible == n or retu[possible][0] != cs:
            rs = min(h-1,rs+l)
        else:
            rs = min(retu[possible][1]-1,rs+l)     
    print(rs+1,cs+1)


