n = int(input())
s = input()

maru = 0
batu = 0
for i in s:
    if i == 'o':
        maru += 1
    elif i == 'x':
        batu += 1
if maru > 0 and batu == 0:
    print("Yes")
else:
    print("No")