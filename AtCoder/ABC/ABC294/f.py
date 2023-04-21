def is_sosuu(x):
    if x == 1:
        return False
    for i in range(2,x):
        if x % i == 0:
            return False
    return True
a = int(input("数："))
if is_sosuu(a):
    print("素数です")
else:
    print("素数ではない")