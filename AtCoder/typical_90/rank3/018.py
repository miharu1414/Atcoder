# パス

t = int(input())
l,x,y = map(int,input().split())
q = int(input())
e = [int(input()) for i in range(q)]
chokoudai = [x,y,0]
pos = [0,0,0]
import math
pi = math.pi
for i in range(q):
    time = e[i]
    pos[1] = -l/2*math.sin(2*pi*e[i]/t)
    pos[2] = l/2-l/2*math.cos(2*pi*e[i]/t)
    dis = 0
    print(pos)
    for j in range(3):
        dis += (pos[j] - chokoudai[j])**2
    b = pos[2]
    a = math.sqrt(dis - b**2)
    ans = math.atan(b/a)
    ans = ans*180/pi
    print(ans)