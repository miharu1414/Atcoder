n = int(input())
a = list(map(int,input().split()))
ans = []
for i in a:
    if i % 2 == 0:
        ans.append(i)
print(*ans)