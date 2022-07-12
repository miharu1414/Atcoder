n = int(input())

LR = []

for i in range(n):
    a,b = map(int,input().split())
    LR.append([a,b])
LR.sort(key=lambda x:x[0])


now_i = 1
right_pos= 0
right = LR[0][1]
left = LR[0][0]
ans = []
if n == 1:
    print(left,right)
    exit()

while 1:
    if LR[now_i][0] <=right:
        if LR[now_i][1] > right:
            right = LR[now_i][1]
            right_pos = now_i
        now_i+=1
    else:
        ans.append([left,right])
        left = LR[now_i][0]
        right = LR[now_i][1]
        right_pos = now_i
        now_i += 1
    if now_i == n:
        ans.append([left,right])
        break
for i in ans:
    print(i[0],i[1])