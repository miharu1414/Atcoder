n = int(input())
a = input().split()
b = ""
for i in range(n):
    b += a[i]
a = b
if not '1' in b:
    print("Yes")
    exit(0)
if (b[1] =='1') & (b[0]=='0'):
    print("Yes")
else:
    print("No")