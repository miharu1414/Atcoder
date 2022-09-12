l,r = map(int,input().split())
mod = 1000000007
ans = 0

if len(str(l)) == len(str(r)):
    print(int(len(str(l))*(r-l+1)%mod*(r+l)%mod*pow(2,-1)%mod))
    exit()
else:

    num = (int(len(str(l))) * ((l + 10**(int(len(str(l))))-1)%mod)*(((10**(int(len(str(l)))))-l)%mod)%mod*pow(2,-1,mod))%mod
    ans = num
    for i in range(int(len(str(l))+1),int(len(str(r)))):
        num = ( i* ((10**(i-1)+10**i-1)%mod)*((10**i-10**(i-1))%mod)%mod*pow(2,-1,mod))%mod
        ans = (ans+num)%mod
    num = ( int(len(str(r)))* ((r+10**(len(str(r))-1))%mod)*((r-10**(len(str(r))-1)+1)%mod)%mod*pow(2,-1,mod))%mod
    ans = (ans+num)%mod
    print(ans)
