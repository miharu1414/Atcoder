s = input()
retu = [1]*7
retu[2] += 1
retu[3]+=1
retu[4] +=1

def T(i):
    if i == 7:
        return 0
    elif i == 4:
        return 1
    elif i == 8 or i == 2:
        return 2
    elif i == 5 or i == 1:
        return 3
    elif i == 9 or i == 3:
        return 4
    elif i == 6:
        return 5
    else:
        return 6

for i in range(10):
    if s[i] == '0':
        retu[T(i+1)] -= 1


left = 0
for i in range(7):
    if retu[i] > 0:
        left = i
        break
right = 0
for i in range(7):
    if retu[6-i] > 0:
        right = 6-i
        break

ok = 0
for i in range(left,right):
    if retu[i] == 0:
        ok = 1
if ok and s[0] == "0":
    print("Yes")
else:
    print("No")