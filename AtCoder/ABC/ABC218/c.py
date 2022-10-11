from math import inf


n = int(input())
s = [input() for i in range(n)]
t = [input() for i in range(n)]


max_x,max_y,min_x,min_y  = 0,0,inf,inf
count_s,count_t = 0,0
for i in range(n):
    for j in range(n):
        if s[i][j] == '#':
            max_x = max(max_x,i)
            max_y = max(max_y,j)
            min_x = min(min_x,i)
            min_y = min(min_y,j)
            count_s +=1
        if t[i][j] == '#':
            count_t += 1
if count_t != count_s:
    print("No")
    exit()
ar1 = []
for i in range(min_x,max_x+1):
    A = []
    for j in range(min_y,max_y+1):
        A.append(s[i][j])
    ar1.append(A)

S = ar1
ar2 =[]
for x in zip(*S[::-1]):

    ar2.append(list(x))

S = ar2
ar3 =[]
for x in zip(*S[::-1]):

    ar3.append(list(x))

S = ar3
ar4 = []
for x in zip(*S[::-1]):

    ar4.append(list(x))



max_x,max_y,min_x,min_y  = 0,0,inf,inf
for i in range(n):
    for j in range(n):
        if t[i][j] == '#':
            max_x = max(max_x,i)
            max_y = max(max_y,j)
            min_x = min(min_x,i)
            min_y = min(min_y,j)

ar5 = []
for i in range(min_x,max_x+1):
    A = []
    for j in range(min_y,max_y+1):
        A.append(t[i][j])
    ar5.append(A)

if ar5 == ar1 or ar5 == ar2 or ar5 == ar3 or ar5 == ar4:
    print("Yes")
else:
    print("No")