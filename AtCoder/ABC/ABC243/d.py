n,x = map(int,input().split())
s = input()
now = x

from collections import deque

d = deque()


for i in range(n):
    if len(d)==0:
        d.append(s[i])
    
    elif s[i] == "U":
        mae = d.pop()
        if mae == 'U':
            d.append(mae)
            d.append('U')
    else:
        d.append(s[i])
d_list = list(d)
for i in range(len(d_list)):
    if d_list[i] == 'U':
        now //= 2
    elif d_list[i] == 'R':
        now = now*2 + 1
    else:
        now = now*2
print(now)

