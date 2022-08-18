n = int(input())
G = [[] for i in range(n)]
count = dict()
for i in range(n-1):
    a,b = map(int,input().split())

    if (a) not in count:
        count[a] = 1
    else:
        count[a] += 1
    if b not in count:
        count[b] = 1
    else:
        count[b] += 1    
for key in count.keys():
    if count[key] == n-1:
        print("Yes")
        exit()
print("No")
    