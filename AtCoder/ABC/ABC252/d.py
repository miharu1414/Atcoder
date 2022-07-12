n = int(input())
a = list(map(int,input().split()))
a.sort()
a_count  = []
for i in range(n):
    if i == 0:
        count = 1
        pre = a[i]
        continue
    elif pre != a[i]:
        a_count.append([pre,count])
        count = 1
        pre = a[i]
    
    else:
        count+=1      
a_count.append([pre,count])
size = len(a_count)
Sum = [0]*size
Sum[0] = a_count[0][1]



for i in range(1,size):
    Sum[i] = Sum[i-1]+a_count[i][1]

ans = 0

for i in range(1,size-1):
    pre_count = Sum[i-1]
    Back_count  = Sum[size-1]-Sum[i]
    ans += pre_count * Back_count * a_count[i][1]
print(ans)