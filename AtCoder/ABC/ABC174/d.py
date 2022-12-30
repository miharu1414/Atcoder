n = int(input())
s = input()

cnt = 0
for i in s:
    if i == 'R':
        cnt += 1

x = 0
for i in range(len(s)):
    if s[i] == 'W' and i < cnt:
        x += 1
print(x)