n,k = map(int,input().split())
ans = 1
mod = 10**9+7
if n==1:
    print(k)
elif n ==2:
    if k == 1:
        print(0)
    else:
        print(k*(k-1)%mod)
else:
    ans *= k*(k-1)%mod
    ans = ans*  pow(k-2,n-2,mod)%mod
    print(ans)