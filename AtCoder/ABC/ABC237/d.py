from operator import le


n = int(input())
s = input()

ans = [0]*(n+1)
right_pos = n
left_pos = 0
mae = 0
for i in range(n):
    if s[i]=='L':
        ans[right_pos] = mae
        mae = i+1
        right_pos -= 1
        if i == n-1:
            ans[right_pos] = mae

    else:
        ans[left_pos] = mae
        mae = i+1
        left_pos += 1
        if i == n-1:
            ans[left_pos] = mae
print(*ans)