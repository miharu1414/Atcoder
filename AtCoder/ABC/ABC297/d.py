a, b = map(int, input().split())
if a < b:
    a,b = b,a
if a == b:
    print(0)
    exit()
first = 0
if a % b != 0:
    first = a//b
    a %= b
if a % b ==0:
    print(a//b - 1)
    exit()
second = 0

while a != b:
    if a>b:
        a -= b
    else:
        b -= a
    second += 1
    if a==b:
        break
    if a < b:
        a,b = b,a
    if a != 0 and b!= 0 and a % b != 0 :
        first += a//b
        a %= b
    if a != 0 and b!= 0 and a % b == 0 :
        first += a//b - 1
        break

print(first+second)
