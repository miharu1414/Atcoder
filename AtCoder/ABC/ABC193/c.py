


n = int(input())

i = 2
possible = set()
while i *i <= n:
    j = 2
    while i ** j<=n:
        possible.add(i**j)
        j+=1
    i+=1
print(n-len(possible))
        