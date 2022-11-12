n, m = map(int,input().split())
h = list(map(int,input().split()))
w = list(map(int,input().split()))

h.sort()
w.sort()

sum1 = [0]*(n//2)
for i in range(n//2):
    if i == 0:
        sum1[i] = abs(h[2*i]-h[2*i+1])
    else:
        sum1[i] = sum1[i-1]+abs(h[2*i]-h[2*i+1])

sum2 = [0]*(n//2)
for i in range((n-1)//2):
    if i == 0:
        sum2[i] = abs(h[2*i+1]-h[2*i+2])
    else:
        sum2[i] = sum2[i-1] + abs(h[2*i+1]-h[2*i+2])


import bisect
ans = 1<<60 
if n == 1:
    ans = 1<<60
    for i in range(m):
        ans = min(ans,abs(w[i]-h[0]))
    print(ans)
    exit()
for i in range(len(w)):
    now = w[i]
    idx = bisect.bisect_left(h,now)

    if idx == 0 or idx == 1:
        ans = min(ans,abs(h[0]-now)+sum2[len(sum2)-1])
    elif idx == n:
        ans = min(ans,abs(h[len(h)-1]-now)+sum1[len(sum1)-1])
    else:
        if idx%2==0:
            ans = min(ans,abs(h[idx]-now)+sum1[idx//2-1]+ (sum2[len(sum2)-1] - sum2[idx//2-1]))
           
        else:
            ans = min(ans,abs(h[idx-1]-now)+sum1[idx//2-1]+(sum2[len(sum2)-1] - sum2[idx//2-1]))
   

print(ans)