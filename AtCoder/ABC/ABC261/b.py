n = int(input())
a  = [input() for i in range(n)]
cnt = 0

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if a[i][j] == "D" and a[j][i] != "D":
            cnt += 1
        if a[i][j] == "W" and a[j][i] != "L":
            cnt+=1
        if a[i][j] == "L" and a[j][i] != "W":
            cnt +=1
if cnt:
    print("incorrect")
else:
    print("correct")
