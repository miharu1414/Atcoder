s = input()
s1 = ''
nr = []


from collections import deque

nl = deque()
num = dict()
tyokuzen = []
for i in range(len(s)):
    if s[i] == '(':
        nl.append(i)
    elif s[i] ==')':
        tyokuzen.append(nl.pop())

nl = tyokuzen

hako = []
ok = 1
numr = 0
numl = 0
from collections import defaultdict
d = defaultdict(list)

for i in range(len(s)):
    if 'a' <= s[i] <= 'z':
        if s[i] in num and num[s[i]] != -1:    
            ok = 0
            break
        else:
            if len(nl)!=0:
                d[nl[numr]].append(i)
            num[s[i]] = i
        
        
    elif s[i] == '(':
        numl += 1
        continue
    
    else:
        
        start = nl[numr]
        for k in d[start]:
            num[s[k]] = -1

        numr += 1
if ok :
    print("Yes")
else:
    print("No")