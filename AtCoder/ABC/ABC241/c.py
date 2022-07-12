n = int(input())
s = [input() for i in range(n)]

flag = 0
for i in range(n):
    num = 0
    for j in range(n):
        if s[i][j] == '#':
            num += 1
        if j >=6:
            if s[i][j-6]=="#":
                num -=1
        if num >= 4:
            flag = 1
        
for i in range(n):
    num = 0
    for j in range(n):
        if s[j][i] == '#':
            num += 1
        if j >=6:
            if s[j-6][i]=="#":
                num -=1
        if num >= 4:
            flag = 1

for i in range(n):
    if n - i>=6:
        num = 0
        for j in range(n):
            if i+j >=n:
                break
            if s[j][i+j] == '#':
                num += 1
            if j >=6:
                if s[j-6][i+j-6]=="#":
                    num -=1
            if num >= 4:
                flag = 1
        num = 0
        for j in range(n):
            if i+j >=n:
                break
            if s[i+j][j] == '#':
                num += 1
            if j >=6:
                if s[i+j-6][j-6]=="#":
                    num -=1
            if num >= 4:
                flag = 1

for i in range(n):
    if i>=5:
        num = 0
        for j in range(i+1):

            if s[i-j][j] == '#':
                num += 1
            if j>=6:
                if s[i-j+6][j-6]=="#":
                    num -=1
            if num >= 4:
                flag = 1
        num = 0
    
        for j in range(i+1):
            if i+j >=n:
                break
            if s[n-j-1][i-5+j] == '#':
                num += 1
            if j >=6:
                if s[n-1-j+6][i-5+j-6]=="#":
                    num -=1
            if num >= 4:
                flag = 1

if flag:
    print("Yes")
else:
    print("No")