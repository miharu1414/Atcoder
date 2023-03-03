n, m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

Sum = 0
for solved in b:
    Sum += a[solved-1]
print(Sum)