n , m =map(int,input().split())
s = [input() for i in range(n)]
t = [input() for i in range(m)]
cnt = 0
for i in range(n):
    flag = 0
    for j in range(m):
        if s[i][-3:] == t[j]:
            flag = 1
    if flag: cnt += 1
print(cnt)