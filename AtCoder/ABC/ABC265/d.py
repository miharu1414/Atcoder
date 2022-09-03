n,p,q,r = map(int,input().split())
a = list(map(int,input().split()))

ruiseki = [0]*(n+1)
for i in range(1,n+1):
    if i == 0:
        ruiseki[i] = a[i-1]
    else:
        ruiseki[i] = a[i-1] + ruiseki[i-1]


# ステップ１　二分探索
import bisect

sum = p+q+r


def search(start,end):
    i = start
    x,y,z = 0,0,0
    while x < p:
        x += a[i]
        i+=1
    while y < q:
        y += a[i]
        i+=1
    if x == p and y == q:
        return True
    else:
        return False
ans = 0
for i in range(n+1):
    now = ruiseki[i]
    idx = bisect.bisect_left(ruiseki,now - sum)
    if now - ruiseki[idx] == sum:
        if search(idx,i) == True:
            ans = 1
            break
if ans:
    print("Yes")
else:
    print("No")
