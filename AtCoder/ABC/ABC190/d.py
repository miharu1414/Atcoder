n = int(input())
div  = []
i = 2
while i*i<=n:
    if n % i ==0:
        if i &1:
            div.append(i)
        if i * i != n:
            if n//i & 1:
                div.append(n//i)

    i += 1

ans = 0
if n != 1:
    ans += 1
for i in range(len(div)):
    if n % div[i]==0:
        ans += 1
    
if n & 1:
    ans += 1
print(ans*2)
        
    