n = int(input())
a = list(map(int,input().split()))
q = int(input())
Q = []
for i in range(q):
    t,y,u = map(int,input().split())
    Q.append([t,y,u])

suuretsu = []
for i in range(n):
    suuretsu.append([a[i],i])
suuretsu.sort()


def nibun_max(i,x):
    def is_ok(mid):
        if mid > n:
            return False
        if mid <0:
            return True
        if suuretsu[mid][0]<x:
            return 1
        if suuretsu[mid][0]==x and suuretsu[mid][1]<=i:
            return 1
        return False
    ok = -1
    ng = n
    while ng-ok > 1:
        mid = (ok+ng) // 2 # 平均(小数切り捨て)
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

def nibun_min(i,x):
    def is_ok(mid):
        if mid > n:
            return False
        if mid <0:
            return True
        if suuretsu[mid][0]<x:
            return 1
        if suuretsu[mid][0]==x and suuretsu[mid][1]<=i:
            return 1
        return False
    ok = n
    ng = -1
    while ng-ok > 1:
        mid = (ok+ng) // 2 # 平均(小数切り捨て)
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

for i in range(q):
    l,r ,x = map(int,Q[i])
    print(x,nibun_max(r-1,x),nibun_max(l-2,x))
    
    if suuretsu[nibun_max(r-1,x)][0] != x:
        print(0)
        continue
    right = nibun_max(r-1,x)
    if right <0:
        print(0)
        continue
    left = nibun_max(l-2,x)
    if left < 0:
        left = 0
    print(right-left+1) 