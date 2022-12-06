n = int(input())

cnt = 0

for a in range(1,n):
    b_cnt = (n-1)//a
    cnt += b_cnt
print(cnt)