n = int(input())
s = input()
foe = 0
for i in range(n-1):
    if s[i] == s[i+1]:
        foe = 1
if foe:
    print("No")
else:
    print("Yes")