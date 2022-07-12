s = input()
t = input()

from collections import deque

d = []

d.append([s[0],1])
pos1 = 0 
for i in range(1,len(s)):
    now = d[pos1]
    if s[i] == now[0]:
        d[pos1][1] += 1

    else:
        pos1 += 1
        new = [s[i],1]
        d.append(new)

d2 = []

d2.append([t[0],1])
pos2 = 0
for i in range(1,len(t)):
    now = d2[pos2]
    if t[i] == now[0]:
        d2[pos2][1] += 1

    else:
        pos2 += 1
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
        