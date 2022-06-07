a,b = map(int,input().split())
import math
lcm = a*b//math.gcd(a,b)
if lcm>10**18:
    print("Large")
else:
    print(lcm)
