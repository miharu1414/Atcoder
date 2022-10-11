n = int(input())
a = list(map(int,input().split()))

kisuu =[]
guusuu = []
for i in range(n):
    if a[i]%2==0:
        guusuu.append(a[i])
    else:
        kisuu.append(a[i])

if len(guusuu)<2 and len(kisuu)<2:
    print(-1)
    exit()

maxa = 0
guusuu.sort(reverse=True)
kisuu.sort(reverse=True)
if len(guusuu)>=2:
    maxa = max(maxa,guusuu[0]+guusuu[1])
if len(kisuu)>=2:
    maxa = max(maxa,kisuu[0]+kisuu[1])
print(maxa)