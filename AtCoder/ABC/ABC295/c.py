n = int(input())
a = list(map(int, input().split()))

colorSet = set()
ansCount = 0
for i in range(n):
    if a[i] not in colorSet:
        colorSet.add(a[i])
    else:
        ansCount += 1
        colorSet.discard(a[i])
print(ansCount)
