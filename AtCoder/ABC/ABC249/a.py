a,b,c,d,e,f,x = map(int,input().split())
dis_a = 0
dis_b = 0
time = x
mod_a = a+c
mod_b = d+f
dis_a += x//mod_a*a*b + min(x%mod_a*b,a*b)
dis_b += x//mod_b*d*e + min(x%mod_b*e,d*e)
if dis_a > dis_b:
    print("Takahashi")
elif dis_a<dis_b:
    print("Aoki")
else:
    print("Draw")