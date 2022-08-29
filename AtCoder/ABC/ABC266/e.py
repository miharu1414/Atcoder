n = int(input())
En = 0
for i in range(n):
    En_1 = 0
    for j in range(6):
        En_1 += max(j+1, En)/6
    En = En_1
print(En)