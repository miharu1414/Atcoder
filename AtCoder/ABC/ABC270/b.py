x,y,z = map(int,input().split())
if x < 0:
    x *= -1
    y *= -1
    z *= -1
if x < y or y < 0:
    print(x)
    exit()
if z > 0 and y > z and x > y:
    print(x)
    exit()
if y > 0 and y < x and z < 0:
    print(2*abs(z) + x)
else:
    print(-1)