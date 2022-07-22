n = int(input())
l = []
a = []

for i in range(n):

    A =list(map(int,input().split()))
    a.append(tuple(A))


kinds = 0
list = dict()
for i in range(n):
    if a[i] not in list:
        kinds += 1
        list[a[i]] = 1
    else:
        list[a[i]] += 1
print(kinds)
    