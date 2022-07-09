from re import L


n = int(input())
s = input()
w = list(map(int,input().split()))

adult =[]
young = []

for i in range(n):
    if s[i]=='1':
        adult.append(w[i])
    else:
        young.append(w[i])

adult.sort()

import bisect
max_score = 0
if len(adult) ==0 or len(young) == 0:
    print(n)
    exit()
young.append(0)
young.sort()
for i in range(len(young)):
    sep = young[i]
    pos = bisect.bisect_left(adult,sep+0.5)
    score = (len(adult)-pos) + (i+1-1)
    if max_score<score:
        max_score = score
    
print(max_score)