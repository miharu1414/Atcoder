
def modinv(a,m):
    b,u,v = m,1,0
    while b:
        t = a//b
        a -= t*b
        a,b = b,a
        u -= t*v 
        u,v = v,u
    u %= m
    if u < 0:
        u += m
    return u





l, r = map(int,input().split())

mod = 1000000007
sizel = len(str(l))
sizer = len(str(r))
ans = 0
b = modinv(2,mod)

if sizel != sizer:
    num = (int(sizel) * ((l + 10**(int(sizel))-1)%mod)*(((10**(int(sizel)))-l)%mod)*b)%mod
    ans += num

    for i in range(int(sizel+1),int(sizer)):
        num = ( i* ((10**(i-1)+10**i-1)%mod)*((10**i-10**(i-1))%mod)*b)%mod
        ans = (ans+num)%mod
    
    num = ( int(sizer)* ((r+10**(sizer-1))%mod)*((r-10**(sizer-1)+1)%mod)*b)%mod
    ans = (ans+num)%mod

else:
    ans = (int(sizer)*((l+r)%mod) *((r-l+1)%mod)*b)%mod

print(ans)