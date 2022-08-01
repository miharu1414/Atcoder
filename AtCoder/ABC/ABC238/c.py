n = int(input())
keta = 0
N = n
while N:
    N//=10
    keta += 1

mod = 998244353
ans = 0
for i in range(keta):
    if i == keta-1:
        kaku = 0
        while 1:
            if kaku == 10**(i)-1:
                break
            kaku = 10*kaku + 9

        cnt = (1+n-kaku)%mod*(n-kaku)%mod*pow(2,-1,mod)%mod
        ans = (ans+cnt)%mod
        break
    cnt = 9*10**(i)%mod*(1+9*10**(i)%mod)*pow(2,-1,mod)%mod
    ans = (ans+cnt)%mod

print(ans)