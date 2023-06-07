n = int(input())
s1 = [map(str,input().split()) for i in range(n)]
s,a = [list(i) for i in zip(*s1)]
min_i = 0

now = int(a[0])

for i in range(n):
    if now > int(a[i]):
        min_i = i
        now = int(a[i])
for i in range(min_i,n):
    print(s[i])
for i in range(0,min_i):
    print(s[i])