n = int(input())
s = [input() for i in range(n)]
tokuhyo = dict()
name = s[0]
max_n = 0
for i in s:
    if i not in tokuhyo:
        tokuhyo[i] = 1
        if max_n < tokuhyo[i]:
            max_n = tokuhyo[i]
            name = i
    else:
        tokuhyo[i] += 1
        if max_n < tokuhyo[i]:
            max_n = tokuhyo[i]
            name = i
print(name)