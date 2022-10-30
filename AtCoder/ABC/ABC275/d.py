n = int(input())

if n == 0:
    print(1)
    exit()

num_2 = 0
num_3 = 0
n2 = n
n3 = n

while True:
    if n2 // 2 >0:
        n2 //= 2
        num_2 += 1
    if n3 // 3 > 0:
        n3 //= 3
        num_3 += 1
    if n2 // 2 == 0 and n3 // 3 == 0:
        break
print(num_2,num_3)
