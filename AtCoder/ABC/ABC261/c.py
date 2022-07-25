n = int(input())
s = [input() for i in range(n)]
d = dict()
for i in range(n):
    now = s[i]
    if now in d:
        print(now+'('+ str(d[now])+')')
        d[now] += 1
    else:
        print(now)
        d[now] = 1
    