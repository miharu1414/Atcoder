s = input()
t = input()

score = [0]*len(t)

for i in range(len(t)):
    if s[len(s)-len(t)+i] == t[i] or s[len(s)-len(t)+i] =='?' or t[i] == '?':
        score[i] = 1
Sum = sum(score)
if Sum == len(t):
    print("Yes")
else:
    print("No")
for i in range(len(t)):
    Sum -= score[i]
    if s[i] == t[i] or s[i]=='?' or t[i] =='?':
        score[i] = 1
        Sum += 1
    else:
        score[i] = 0
    if Sum == len(t):
        print("Yes")
    else:
        print("No")
        
    