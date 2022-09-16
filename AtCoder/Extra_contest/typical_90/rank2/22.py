a,b,c = map(int,input().split())
import math
mod = math.gcd(a,math.gcd(b,c))
count = 0
count += a/mod-1
count += b/mod -1
count+= c/mod -1
print(int(count))