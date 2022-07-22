s = input()
g = dict()
for i in range(3):
    if s[i] not in g:
        g[s[i]] = 1
    else:
        g[s[i]] += 1
for i in range(3):
    if g[s[i]] == 1:
        print(s[i])
        exit()

print(-1)


