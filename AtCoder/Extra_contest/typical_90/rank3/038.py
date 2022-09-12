a,b = map(int,input().split())
import math
gcd = math.gcd(a,b)
r  = b / gcd
if r <= int((1000000000000000000)//a):
    print(a*b//gcd)
else:
    print('Large')