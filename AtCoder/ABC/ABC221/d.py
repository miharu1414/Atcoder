n = int(input())
ab = [map(int,input().split()) for i in range(n)]
a,b = [list(i) for i in zip(*ab)]
 
imos = []
for i in range(n):
    imos.append([a[i],1])
    imos.append([b[i]+a[i],-1])
 
ans = [0]*(n+1)
num = 0
imos.sort()
 
 
before = imos[i][0]
i = 0
num = 1
while i<2*n-1 and imos[i][0] == imos[i+1][0]:
    if imos[i][1] == 1:
         num+=1
    else:
        num-=1
    i+=1
 
while i < 2*n:
	
	if i==2*n - 1:
		break
	ans[num] += imos[i+1][0] - imos[i][0]
	i+=1
	if imos[i][1] == 1:
		num+=1
	else:
		num-=1
	while i<2*n-1 and imos[i][0] == imos[i+1][0]:
	   if imos[i+1][1] == 1:
	       num+=1
	   else:
	       num-=1
	   i+=1	
ans2 =[0]*n
for i in range(1,len(ans)):
	ans2[i-1]=ans[i]
print(*ans2)