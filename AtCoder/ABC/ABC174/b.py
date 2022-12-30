n,d = map(int,input().split())
xy = [map(int,input().split()) for i in range(n)]
x,y = [list(i) for i in zip(*xy)]

def dif(a,b):
    return (a**2+b**2)**(1/2)

ans  = 0
for i in range(n):
    if dif(x[i],y[i])<=d:
        ans += 1
print(ans)