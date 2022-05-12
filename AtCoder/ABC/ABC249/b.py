from re import L


s = input()
moji = dict()
ok = 1
ok2 = 0
ok3 = 0
for i in s:
    if i in moji:
        ok = 0
    else:
        moji[i] = 1
if ok == 1 and not (s.islower()) and not(s.isupper()):
    print('Yes')
else:
    print("No")
