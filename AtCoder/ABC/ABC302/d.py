n, m, d = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort()
b.sort()
ans = []
import bisect
for i in range(n):
    a_pre = a[i]
    b_idx = bisect.bisect_left(b,d + a_pre)

    for j in range(-1,2,1):
        if b_idx+j < m and b_idx+j >= 0 and abs(b[b_idx+j]-a_pre)<=d:
            ans.append(b[b_idx+j]+a_pre)
    b_idx = bisect.bisect_left(b,d - a_pre)
    for j in range(-1,2,1):
        if b_idx+j < m and b_idx+j >= 0 and abs(b[b_idx+j]-a_pre)<=d:
            ans.append(b[b_idx+j]+a_pre)
try:
    print(max(ans))
except:
    print(-1)
    