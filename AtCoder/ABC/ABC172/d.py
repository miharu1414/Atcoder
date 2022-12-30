n = int(input())

a = [0]*(n+1)
for i in range(1,n+1):
     now = (n//i)*(i+n//i*i)//2 
     a[i] = now
print(sum(a))