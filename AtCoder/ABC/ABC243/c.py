n = int(input())
xy = [map(int, input().split()) for _ in range(n)]
x, y = [list(i) for i in zip(*xy)]
s = input()
key = {}
for i in range(n):
    if s[i] == 'R':
        if y[i] in key.keys() and x[i] < key[y[i]]:
            key[y[i]] = x[i]
        else:
            key[y[i]] = x[i]
count = 0
for i in range(n):
    if s[i] == 'L':
        if y[i] in key.keys() and x[i] >= key[y[i]]:
            count += 1

if count > 0:
    print("Yes")
else:
    print("No")