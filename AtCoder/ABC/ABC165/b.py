x = int(input())
now = 100
i = 1
while 1:
    now *= 101
    now//=100
    now = int(now)
    if now>=x:
        print(i)
        exit()
    i += 1
    