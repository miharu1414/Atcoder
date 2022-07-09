a,b,d = map(int,input().split())
import math
d_rad = d*math.pi/180
x = a*math.cos(d_rad) -b *math.sin(d_rad)
y = a*math.sin(d_rad) +b*math.cos(d_rad)
print(x,y)
