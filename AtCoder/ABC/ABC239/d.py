n =200
p = [i for i in range(n + 1)]

for i in p[3:]:
    if p[i] % 2 == 0:
        p[i] = 0

root_n = n ** 0.5
for i in range(3, n):
    if i > root_n:
        break
    if p[i] != 0:
        for j in range(i, n + 1, 2):
            if i * j >= n + 1 :
                    break
            p[i * j] = 0
plist = sorted(list(set(p)))[2:]


a,b,c,d = map(int,input().split())
min = a+c
max = b+d
ans = 0
for i in range(a,b+1):
    flag = 0
    for j in range(c,d+1):
        if i+j in  plist:
            flag = 1
    if flag == 0:
        ans = 1
if ans == 0 :
    print("Aoki")
else:
    print("Takahashi")
