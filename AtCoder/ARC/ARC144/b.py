n,a,b = map(int,input().split())
A = list(map(int,input().split()))
A.sort()

mean = sum(A)/n
cnt1,cnt2 = 0,0
for i in range(n):
    cnt1,cnt2 = 0,0
    if A[i] < mean:
        cnt1 = (mean-A[i])//a
    else:
        cnt2 = (A[i]-mean)//b