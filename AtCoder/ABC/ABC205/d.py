n,q = map(int,input().split())
a  = list(map(int,input().split()))
K  = [int(input()) for i in range(q)]


for i in range(q):
    now = K[i]
    
b = []
before = 0
kuhaku = dict()
for i in range(n):
    if i == 0:
        blank = a[i] - before 
        b.append(blank)
        before = a[i]
        kuhaku[a[i]] = blank
    else:
        blank = a[i] -  before - 1
        ans = kuhaku[before] + blank
        b.append(ans)
        before = a[i]   
        kuhaku[a[i]] =   ans

kouho = []
before = 0



henkan = dict()

for k,v in kuhaku.items():
    henkan[v] = k
for k,v in henkan.items():
    kouho.append(k)
import bisect
henkan[0] = 0

for i in range(q):
    now = K[i]
    maxa = bisect.bisect_right(kouho,now)
    if maxa == 0:
        print(now)
    else:
        print( henkan[kouho[maxa-1]] +now - kouho[maxa-1]+1)
    