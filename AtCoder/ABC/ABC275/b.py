a,b,c,d,e,f = map(int,input().split())
mod =  998244353 
a %= mod 
b %= mod 
c %= mod
d %= mod
e %= mod
f %= mod
A = ((a * b)%mod * c)%mod
B = ((d*e)%mod * f)%mod
print((A-B)%mod)