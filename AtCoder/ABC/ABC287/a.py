n = int(input())
s = [input() for i in range(n)]
fo = 0
for i in range(n):
    if 'F' in s[i]: fo +=1
if fo > n//2:
    print("Yes")
else:print("No")