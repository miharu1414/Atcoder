# https://atcoder.jp/contests/typical90/tasks/typical90_bq

n, k = map(int,input().split())
def pow(a,n,p):
    bi = str(format(n,"b"))#2進表現に
    res = 1
    for i in range(len(bi)):
        res = (res*res) %p
        if bi[i] == "1":
            res = (res*a) %p
    return res
mod = 1000000007
a = k*(k-1)%mod
b = pow(k-2,n-2,mod)
if n == 1:
    print(k)
elif n==2:
    print(k*(k-1)%mod)
else:
    print(a*b%mod)