n,a,b = map(int,input().split())
import math
count_a = n//a
count_b = n//b
ab = a*b//math.gcd(a,b)
count_ab = n//(ab)

sum_n = (n+1)*n//2
sum_a = (a+count_a*a)*count_a//2  
sum_b = (b+count_b*b)*count_b//2
sum_ab = (ab+count_ab*ab)*count_ab//2

print(int(sum_n-sum_a-sum_b+sum_ab))