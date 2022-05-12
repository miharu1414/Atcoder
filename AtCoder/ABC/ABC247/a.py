s = input()
for i in range(3):
    s[i+1] = s[i]
s[0] = 0
print(s)