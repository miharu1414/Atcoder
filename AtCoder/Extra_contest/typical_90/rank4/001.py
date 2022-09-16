def nibun(m,n,a,l,k):
    cnt = 0
    pre_pos= 0
    for i in range(n):
        if a[i]-pre_pos >=m and l - a[i]>=m:
            cnt += 1
            pre_pos = a[i]

    if cnt >= k:
        return 1
    else:
        return 0

n, l = map(int,input().split())
k = int(input())
a = list(map(int,input().split()))
right,left  = l+1,-1

while(right-left>1):
    mid = (right+left)//2

    if nibun(mid,n,a,l,k):
        left = mid
    else:
        right = mid
    
print(left)

