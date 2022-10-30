n,x,y = map(int,input().split())
a = list(map(int,input().split()))

g1 = []
g2 = []
for i in range(n):
    if i&1:
        g2.append(a[i])
    else:
        g1.append(a[i])

tyouten = []
now_x,now_y = 0,0
num_y = 0
num_x = 0

zahyou = []
for i in range(n):
    if i&1:
        now_y += g2[num_y]
        num_y += 1
    else:
        now_x += g1[num_x]
        num_x += 1
    zahyou.append((now_x,now_y))

ans = set()

def sentaisyo1(nx,ny,c,d):
    return (nx,2*d-ny)
def sentaisyo2(nx,ny,c,d):
    return (2*c-nx,ny)
def tentaisyo(nx,ny,c,d):
    return(2*c-nx,2*d-ny)

ans.add((now_x,now_y))
from collections import deque

d = deque([])

z = [(now_x,now_y)]
d.append((now_x,now_y))
for i in range(n):
    wx,wy = zahyou[i]
    new = []
    for nx,ny in z:
        now_x, now_y = nx,ny
        a1 = sentaisyo1(now_x,now_y,wx,wy)
        a2 = sentaisyo2(now_x,now_y,wx,wy)
        a3 = tentaisyo(now_x,now_y,wx,wy)

        if a1 not in ans:
            ans.add(a1)
            new.append(a1)
        if a2 not in ans:
            ans.add(a2)
            new.append(a2)
        if a3 not in ans:
            new.append(a3)
            ans.add(a3)
    for X,Y in new:
        z.append((X,Y))
if (x,y) in ans:
    print("Yes")
else:
    print("No")