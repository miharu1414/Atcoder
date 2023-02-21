n = int(input())
s = n%10
if s in [0,1,6,8]:
    print('pon')
elif s == 3:
    print('bon')
else:
    print("hon")