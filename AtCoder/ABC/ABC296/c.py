n, x = map(int,input().split())
a = list(map(int,input().split()))

num = set()
for i in range(n):
    num.add(a[i])
for i in range(n):
    if a[i] + x in num:
        print("Yes")
        exit()
print("No")