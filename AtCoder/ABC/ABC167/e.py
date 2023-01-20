
def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

mod = 998244353 #出力の制限
N = 10**6
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )

def pow(a,n,p):
    bi = str(format(n,"b"))#2進表現に
    res = 1
    for i in range(len(bi)):
        res = (res*res) %p
        if bi[i] == "1":
            res = (res*a) %p
    return res

n, m, k = map(int,input().split())

mod = 998244353
ans = [0]*n
for i in range(k+1):
    ans[i] =  (cmb(n-1,i,mod)*m* pow(m-1,n-i-1,mod))%mod
A = 0
for i in range(k+1):
    A = (A + ans[i])%mod
print(A)