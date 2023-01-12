n = int(input())
a = list(map(int,input().split()))
Sum_x = [0]*n
Sum = sum(a)
ans_x = [0]*n
for i in range(1,n,2):
    Sum -= 2*a[i]
ans_x[0] = Sum
for i in range(1,n):
    ans_x[i] = 2*a[i-1] - ans_x[i-1]
print(*ans_x)