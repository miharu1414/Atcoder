s = input()
t = input()
if s == t:
    print("Yes")
    exit()

ans = 0
before = -1
for i in range(len(s)-1):
    ans = s[:i]+s[i+1:i+2]+s[i:i+1]+s[i+2:]
    if ans == t:
        print("Yes")
        exit()
print("No")