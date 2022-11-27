h,w = map(int,input().split())
s = [input() for i in range(h)]
t = [input() for i in range(h)]

dic = dict()
S_t = []
for i in range(w):
    ans  = ""
    for j in range(h):
        ans += s[j][i]
    if ans in dic:
        dic[ans] += 1
    else:
        dic[ans] = 1

dic2 = dict()
for i in range(w):
    ans  = ""
    for j in range(h):
        ans += t[j][i]
    if ans in dic2:
        dic2[ans] += 1
    else:
        dic2[ans] = 1
        
if dic == dic2:
    print("Yes")
else:
    print("No")