n = int(input())
s = input()

flag = 0
pos = dict()
now_pos = (0,0)
dx = [1,-1,0,0]
dy = [0,0,1,0-1]
def fi(x):
    if x == 'R':
        return 0
    elif x == 'L':
        return 1
    elif x == 'U':
        return 2
    else:
        return 3

pos[now_pos] = 1
for i in range(n):        
    now_pos = (now_pos[0]+dx[fi(s[i])],now_pos[1]+dy[fi(s[i])])
    if now_pos in pos:
        flag = 1
    pos[now_pos] = 1
if  flag:
    print("Yes")
else:
    print("No")