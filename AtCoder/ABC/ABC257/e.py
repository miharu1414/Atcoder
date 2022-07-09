n = int(input())
c = list(map(int,input().split()))

num =[[] for i in range(n+1)]

num_set = set()

pos = 8
newc = []
c_i = []
for i in range(9):
    now = c[i]
    BOO = 1
    for j in range(i+1,9):
        if now>=c[j]:
            BOO = 0
            break
    if BOO:
        newc.append(now)
        c_i.append(i)
    
max_count = 0
num_i =[[] for i in range(n+1)]
for i in range(len(newc)):
    waru = n // newc[i]
    if max_count<waru:
        max_count = waru
    num[waru].append(newc[i])
    num_i[waru].append(i)
ans =[]
score = 0
ans_s = 0
for i in range(len(num[max_count])):
    max = num[max_count][i]
    left = n % max + max
    for i in range(n//max - 1):
        pos = num_i[max_count][i]+1
        ans.append(pos)
    boo = 1
    for j in range(len(newc)):
        if newc[j]<=left and newc[i]>max:
            score = max(newc[i],score)
            boo = 0
            ans.append(num_i[i]+1)
    if boo:
        ans.append(num_i[max_count][i]+1)
    ans.sort(reverse=True)
    s = ''
    for i in ans:
        s += str(i)
    if ans_s < int(s):
        ans_s = int(s)
print(ans_s)


