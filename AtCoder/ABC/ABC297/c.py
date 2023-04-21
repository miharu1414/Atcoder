h, w = map(int, input().split())
s = [list(input().rstrip()) for _ in range(h)]

while True:
    updated = False
    for i in range(h):
        for j in range(w-1):
            if s[i][j] == s[i][j+1] == "T":
                s[i][j] = "P"
                s[i][j+1] = "C"
                updated = True
    if not updated:
        break

for i in range(h):
    print("".join(s[i]))