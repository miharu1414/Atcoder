a,b,h,m = map(int,input().split())

import math
now1 = (h+m/60)/12*360%360
now2 = m/60*360
row = math.radians(now1-now2)

ans = a**2 + b**2 - 2*a*b*math.cos(row)
print(math.sqrt(ans))