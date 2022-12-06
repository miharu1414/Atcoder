s = input()
k = int(input())

l,r = 0,0
left = k
cnt_x = 0
ans = 0
if s[0] == '.':
    left -= 1
import time
cnt = 0
for i in range(len(s)):
    if s[i] == '.':
        cnt += 1
if cnt == len(s) and k == 0:
    print(0)
    exit()
renzoku = 0
maxr = 0
for i in range(len(s)):
    if s[i] == 'X':
        renzoku += 1
    else:
        renzoku = 0
    maxr = max(renzoku,maxr)
if k == 0:
    print(maxr)
    exit()
    
start = time.time()
while r < len(s) and l < len(s):
    end = time.time()
    if end-start > 1.9:
        break
    while left>0 and r + 1 < len(s) :
        if s[r+1]=='X':
            r+=1
        else:
            r += 1
            left -= 1
    while left == 0 and r + 1 < len(s) :
        if s[r+1]=='X':
            r+=1
        else:
            break

    ans = max(ans,r - l + 1)
    if r == len(s)-1:
        break
    if left> 0 and r + 1 < len(s) :
        break
    while left == 0 and l < len(s)-1:
        if s[l]=='X':
            l += 1
        else:
            l += 1
            left += 1
    if l == len(s) - 1:
        break
print(min(len(s),ans))
    
        