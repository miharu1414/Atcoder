n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
count = 0
count_same = 0
b_pos = {}
for i in range(n):
    b_pos[b[i]] = i

for i in range(n):
    if a[i] == b[i]:
        count_same += 1
print(count_same)
for i in range(n):
    if a[i] in b_pos:
        if b_pos[a[i]] != i:
            count+=1
print(count)
