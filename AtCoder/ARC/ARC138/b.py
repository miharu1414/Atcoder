n = int(input())
a = input().split()
b = ""
for i in range(n):
    b += a[i]
a = b
a = int(a,base=2)

if a == 0:
    print("Yes")
    exit(0)

if a < 2**(n-1) and a>= 2**(n-2):
    print("Yes")
else:
    print("No")