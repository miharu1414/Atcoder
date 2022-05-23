n ,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
max_p = -1
for i in range(n):
    if max_p<a[i]:
        max_p = a[i]
max_a = []
for i in range(n):
    if max_p == a[i]:
        max_a.append(i+1)

for j in range(k):
    if b[j] in max_a:
        print("Yes")
        exit()
print("No")