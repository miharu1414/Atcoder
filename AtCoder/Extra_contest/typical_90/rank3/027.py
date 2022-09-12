
n = int(input())
s = [input() for i in range(n)]
apply = dict()
for i in range(n):
    if s[i] not in apply:
        print(i+1)
        apply[s[i]] = 1
    