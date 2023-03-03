n, k = map(int,input().split())
a = list(map(int,input().split()))

b = set(a)
num = 0 
for i in range(5*(10**5)):
    if i not in b or num>=k:
        print(i)
        exit()
    if i in b:
        num += 1
    