n = int(input())
abx = [map(int,input().split())for i in range(n)]
a,p,x = [list(i) for i in zip(*abx)]

ans = 1<<33
for i in range(n):
    if x[i]-a[i]>0:
        ans = min(ans,p[i])
if ans == 1<<33:
    print(-1)
else:
    print(ans)
