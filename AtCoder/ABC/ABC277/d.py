n,m = map(int,input().split())
a = list(map(int,input().split()))
a.sort()

num = dict()
for i in range(n):
    if a[i] not in num:
        num[a[i]] = 1
    else:
        num[a[i]] += 1

Num = []
for k,v in num.items():
    Num.append([k,v])
Num.sort()

i = len(Num)-1

while i >=1:
    if  Num[i][0] == Num[i-1][0]+1:
        i-=1
    else:
        break
All_sum = sum(a)
Sum = []
ren = 0
if n == 1:
    print(0)
    exit()

start_i = i
ika = 0
before = Num[i][0] - 1
ok = 1
while True:
    if i == start_i and ika == 1:
        Sum.append(ren)
        break
    ika = 1
    if Num[i][0] == before+1 or (ok==1 and Num[i][0]==0):
        ren += Num[i][0]*Num[i][1]
    else:
        Sum.append(ren)
        ren = Num[i][0]*Num[i][1]
    before = Num[i][0]

    if i == len(Num)-1:

        if Num[i][0] == m-1:
            ok = 1
        else:
            ok = 0
        i = 0
    else:
        i+=1



ans = max(Sum)
print(All_sum-ans)