s = input()
t = input()

moji_s = dict()
moji_t = dict()

anum_s = 0
anum_t = 0
for i in s:
    if i not in moji_s:
        moji_s[i] = 1
    else:
        moji_s[i] += 1
    if i == '@':
        anum_s += 1
for i in t:
    if i not in moji_t:
        moji_t[i] = 1
    else:
        moji_t[i] += 1
    if i == '@':
        anum_t += 1



flag = 1
atcoder = "atcoder"
for i in s:
    if i == '@':
        continue
    if (i not in moji_t or moji_t[i] == 0 ) and anum_t == 0:
        flag = 0
        break
    elif i in moji_t and moji_t[i] >0:
        moji_t[i] -= 1
    elif i in atcoder:
        anum_t -= 1
    else:
        flag = 0

for k,v in moji_t.items():
    if k != '@':
        if v > 0 and k not in atcoder:
            flag = 0
            break
if flag:
    print("Yes")
else:
    print("No")

