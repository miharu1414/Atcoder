N = int(input())
xy = [map(str, input().split()) for _ in range(N)]
x, y = [list(i) for i in zip(*xy)]

count_name = [0]*N
ans = 0
for i in range(N):
    count = 0
    for j in range(N):
        if i == j:
            continue
        if x[i]==x[j]:
            count += 1
    for j in range(N):
        if i == j:
            continue
        if x[i]==y[j]:
            count += 1
    if count > 0:
        count_name[i] += 1
for i in range(N):
    count = 0
    for j in range(N):
        if i == j:
            continue
        if y[i]==x[j]:
            count += 1
    for j in range(N):
        if i == j:
            continue
        if y[i]==y[j]:
            count += 1
    if count > 0:
        count_name[i] += 1
answer = 1
for i in range(N):
    if count_name[i] == 2:
        answer = 0
        break
if answer:
    print("Yes")
else:
    print("No")