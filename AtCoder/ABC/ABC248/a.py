a = input()
b = []
for i in range(9):
    b.append(int(a[i]))
for i in range(10):
    if i not in b:
        print(i)