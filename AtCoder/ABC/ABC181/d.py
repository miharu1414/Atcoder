S = input()
num = [0]*10
for s in S:
    num[int(s)]+=1

possible = []
if len(S)==1:
    possible.append(str(8))
if len(S) == 2:
    
    for i in range(16,104,+8):
        if '0' not in str(i):
            possible.append(str(i))
else:

        for i in range(104,1008,+8):
            if '0' not in str(i):
                possible.append(str(i))

num2 = [0]*10
for  l in possible:
    for i in range(10): num2[i] = 0
    for s in l:
        num2[int(s)]+=1
    
    ok = 1
    for i in range(1,10):
        if num[i]<num2[i]:
            ok = 0
    if ok:
        print("Yes")
        exit()
print("No")