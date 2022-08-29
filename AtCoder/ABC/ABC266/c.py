a = list(map(int,input().split()))
b= list(map(int,input().split()))
c= list(map(int,input().split()))
d= list(map(int,input().split()))

dx1 = a[0] - c[0]
dy1 = a[1] - c[1]
ok = 1
cnt1 = 0
if dx1 == 0:
    border = a[0]
    if b[0] < border:
        cnt1 += 1
    if d[0] < border:
        cnt1 += 1

else:
    A = dy1 / dx1
    B = -1*A*a[0] + a[1]
    def y(x):
        return A*x + B
    if y(b[0]) < b[1]:
        cnt1 += 1
    if y(d[0]) < d[1]:
        cnt1+=1
if cnt1 != 1:
    ok = 0


dx2 = b[0] - d[0]
dy2 = b[1] - d[1]

cnt1 = 0
if dx2 == 0:
    border = b[0]
    if a[0] < border:
        cnt1 += 1
    if c[0] < border:
        cnt1 += 1

else:
    A = dy2 / dx2
    B = -1*A*b[0] + b[1]
    def y(x):
        return A*x + B
    if y(a[0]) < a[1]:
        cnt1 += 1
    if y(c[0]) < c[1]:
        cnt1+=1
if cnt1 != 1:
    ok = 0
if ok:
    print("Yes")
else:
    print("No")