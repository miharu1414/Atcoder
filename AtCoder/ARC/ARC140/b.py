n = int(input())
s = input()
from collections import deque

d = deque()

sousa = 1
renzoku = 0
ren = []
for i in range(n):

    if len(d)>1:
        a2 = d.pop()
        a1 = d.pop()
        if a1 + a2 + s[i] == "ARC":
            d.append('R') 
            sousa+=1
            renzoku +=1 

        else:
            d.append(a1)
            d.append(a2)
            d.append(s[i])
            if renzoku>0:
                ren.append(renzoku)
            renzoku = 0
    else:
        if renzoku>0:
            ren.append(renzoku)
        renzoku = 0
        d.append(s[i])
if renzoku>0:
    ren.append(renzoku)


num_1 = 0
num_3 = 0
num_2 = 0
ans = 0
num_3v = []
for i in ren:
    if i == 1:
        num_1+=1
    elif i == 2:
        num_2+=2
    else:
        num_3+=i
        num_3v.append(i)
ans = 0
ans += num_2
ans += num_1
ans += max(num_3-2*num_1,0)
print(max(0,ans))
