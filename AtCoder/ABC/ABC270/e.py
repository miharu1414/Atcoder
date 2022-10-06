

n,k = map(int,input().split())
a = list(map(int,input().split()))

taken = []
possible = 0 
for i in range(n):
    if a[i] > 0:
        taken.append(i)
        possible += 1

if possible >= k:
    for i in range(k):
        a[taken[i]] -= 1
    for i in range(n):
        print(*a)
    exit()
left = k - possible
b = a.copy()
i = 0
while 1:
    if left == 0:
        break
    if b[taken[i]] > 1:
        taken.append(taken[i])
        b[taken[i]] -= 1
        left -= 1
    i += 1
for i in taken:
    a[i] -= 1
print(*a)


