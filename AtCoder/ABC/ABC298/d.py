q = int(input())
MOD = 998244353
s = 1
num = 1
erase = 0
hako = [1]

ruijou = [1]*(6*(10**5)+1)

for i in range(6*(10**5)):
    ruijou[i+1] = ruijou[i] * 10 % MOD
for i in range(q):
    c = list(map(int,input().split()))
    if len(c) == 1:
        a = c[0]
    else:
        a = c[0]
        b = c[1]
    
    if a == 1:
        s = (s*10 + b)%MOD
        num += 1
        hako.append(b)
    elif a == 2:
        num -= 1
        s = (s - hako[erase]*ruijou[num])%MOD
        erase += 1

    else:
        print(s)
        
        