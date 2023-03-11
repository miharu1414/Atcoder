n = int(input())
a = list(map(int,input().split()))
called = set()
for i in range(n):
    if i+1 not in called:
        called.add(a[i])
ans = []
for i in range(n):
    if i+1 not in called:
        ans.append(i+1)
print(len(ans))
print(*ans)