def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

factorization(24) 

n = int(input())
a = list(map(int,input().split()))

target = min(a)
a_soinsuu = []

for i in range(n):
    a_soinsuu.append(factorization(a[i]))


# -1の時の判定
hantei = set()
for i in range(n):
    now = a[i]
    while now % 2==0:
        now //= 2
    while now % 3 == 0:
        now //= 3
    hantei.add(now)
if len(hantei) > 1:
    print(-1)
    exit()
    
import math

gcd = a[0]
for i in range(n):
    gcd = math.gcd(gcd,a[i])


b = []
for i in range(n):
    b.append(a[i]//gcd)

cnt = []
ans = 0
for i in range(n):
    cnt = factorization(b[i])
    num = 0
    for j in range(len(cnt)):
        if cnt[j][0]==1:
            continue
        num+=cnt[j][1]
    ans += num
print(ans)
