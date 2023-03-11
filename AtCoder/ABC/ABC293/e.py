a, x, m = map(int,input().split())

factor = []
now = 1
j = 0
start = 0
factor_map = dict()
for i in range(min(10**7,x)):
    if i!=0 and now%m in factor_map:
        j = factor_map[now%m]
        break
    factor.append(now%m)
    factor_map[now%m] = i

    now = (now*a)%m
roop = 0
if j!= 0:
    start = j
    ans = sum(factor[:j])%m
    roop = (x-j)//(len(factor)-j)
    ans = (ans + sum(factor[j:])%m)%m
    
    amari = (x-j)%(len(factor)-j)
    ans = (ans + sum(factor[j:j+amari])%m)%m

    
else:
    ans = sum(factor)%m
    
print(ans%m)