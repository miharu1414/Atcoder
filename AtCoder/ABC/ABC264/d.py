s = list(input())
w = {"a":0,"t":1,"c":2,"o":3,"d":4,"e":5,"r":6}


j = 0
cnt = 0
ans = ['a','t','c','o','d','e','r']
while 1:
    if s == ans:
        break
    for i in range(6):
        if w[s[i]] > w[s[i+1]]:
            s[i],s[i+1] = s[i+1],s[i]
            cnt +=1

print(cnt)
