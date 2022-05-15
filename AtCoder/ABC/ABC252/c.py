n =  int(input())
s = []
T = []
t = []
for i in range(n):
    a,b = map(str,input().split())
    s.append(a)
    t.append(int(b))
poem = dict()
point = t[0]
pos = 0
for i in range(n):
    
    if s[i] in poem:
        continue
    else:
        poem[s[i]] =1
        if t[i]>point:
            point = t[i]
            pos = i
        
print(pos+1)