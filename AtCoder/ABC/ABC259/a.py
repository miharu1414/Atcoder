n,m,x,t,d = map(int,input().split())
now = t
if m >= x:
    print(t)
else:
    dif = x - m
    for i in range(dif):
        now -= d
    print(now)