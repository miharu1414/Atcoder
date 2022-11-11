n = int(input())
xyZ = [map(int,input().split()) for i in range(n)]
x,y,z = [list(i)for i in zip(*xyZ)]


xyz = []
for i in range(1,n):
    xyz.append([x[i],y[i],z[i]])

xyz = sorted(xyz, reverse=True, key=lambda x: x[2])  #[1]に注目してソート


ans = 2<<60

bx,by,bz = x[0],y[0],z[0]
for i in range(n-1):
    ans += abs(x[i]-bx) + abs(y[i])
    