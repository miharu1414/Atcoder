n, k = map(int,input().split())
mod = 10**9+7
ans = 0
ruiseki = [0]*(n+2)
ruiseki[1] = n
ruiseki_mae = [0]*(n+2)
for i in range(1,n+1):
    ruiseki_mae[i+1] = (ruiseki_mae[i] + i )%mod
for i in range(1,n+1):
    ruiseki[i+1] = (ruiseki[i] + n - i)%mod
for i in range(k,n+2):
    Min = ruiseki_mae[i]
    Max = ruiseki[i]
    ans = (ans + Max - Min +1)%mod
    
print(ans)