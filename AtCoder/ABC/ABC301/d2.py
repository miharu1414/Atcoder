s = input()
n = int(input())
idx = []
idx1 = []
now = 0
for i in range(len(s)):
    if s[i] == '?':
        idx.append(len(s)-i-1)
    if s[i] == '1':
        idx1.append(len(s)-i-1)

for i in idx1:
    now += pow(2,i)

if now > n:
    print(-1)
    exit()

for i in idx:
    if now + pow(2,i) <= n:
        now += pow(2,i)
print(now)