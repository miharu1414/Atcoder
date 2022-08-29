n,m,t = map(int,input().split())
a = list(map(int,input().split()))


HP = dict()
for i in range(m):
    x,y = map(int,input().split())
    HP[x-1] = y
now = t
ans = 1
for i in range(n-1):
    if i in HP:
        now += HP[i]
    now -= a[i]
    if now<=0:
        ans = 0
if ans:
    print("Yes")
else:
    print("No")