

n = int(input())
a = list(map(int,input().split()))

if n == 1:
    print(a[0])
    exit()
left_bit_or = [0]*(n+1)
right_bit_or = [0]*(n+1)

left_bit_or[0] = 0
right_bit_or[n] = 0
for i in range(n):
    left_bit_or[i+1] = left_bit_or[i] | a[i]
    right_bit_or[n-i-1] = right_bit_or[n-i] | a[n-i-1]

ans = []
for i in range(n+1):
    ans.append(left_bit_or[i]^right_bit_or[i])

print(min(ans))
    
    