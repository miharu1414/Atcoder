s = input()
t = input()

from collections import deque

d = deque([])

d.append([s[0],1])
for i in range(1,len(s)):
    now = d.pop()
    if s[i] == now[0]:
        now[1] += 1
        d.append(now)
    else:
        d.append(now)
        new = [s[i],1]
        d.append(new)

d2 = deque([])

d2.append([t[0],1])
for i in range(1,len(t)):
    now = d2.pop()
    if t[i] == now[0]:
        now[1] += 1
        d2.append(now)
    else:
        d2.append(now)
        new = [t[i],1]
        d2.append(new)


if len(d) != len(d2):
    print("No")
else:
    flag = 1
    for i in range(len(d)):
        if d[i][0] != d2[i][0]:
            flag = 0
        elif d[i][1] == 1 and d2[i][1]>1:
            flag = 0
        elif d[i][1] > d2[i][1]:
            flag = 0
    if flag:
        print("Yes")
    else:
        print("No")
        