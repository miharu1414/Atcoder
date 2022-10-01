from math import inf


n = int(input())
a = list(map(int,input().split()))
a.sort()
sora = []
num = dict()
count = 0
b = []
for i in range(n):
    if a[i] in num:
        count+=1
    else:
        num[a[i]] = 1
        b.append(a[i])


for i in range(count):
    b.append(inf)
ans = 0
possible = n
hojuu = 0
i = 0
A = []
a = b
while 1:
    target = i + 1
    if a[i-hojuu] == target:
        possible -= 1
        ans += 1
        A.append(a[i-hojuu])
        if possible == 0:
            break
    else:
        hojuu += 1
        possible -= 2
        if possible < 0:
            break
        if possible == 0:
            ans += 1
            A.append(target)
            break
        ans += 1
        A.append(target)
    i+= 1






print(ans)