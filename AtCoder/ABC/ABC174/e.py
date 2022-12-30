n,k = map(int,input().split())
a = list(map(int,input().split()))



left = 0
right = max(a)
import math
def search(x):
    cnt = 0
    for i in range(n):
        cnt += max(math.ceil(a[i]/x) - 1,0)
        if cnt > k:
            return False
    return True
    

while right - left > 1:
    mid = (right + left) // 2
    mid = math.floor(mid)
    if search(mid):
        right = mid
    else:
        left = mid
print(right)