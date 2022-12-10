s = input()
if(len(s)!=8):
    print("No")
    exit()

f = s[0]
e = s[-1]
tyuukan = s[1:-1]

try:
    if f.isupper() and e.isupper() and 100000<= int(tyuukan) <= 999999:
        print("Yes")
    else:
        print("No")
except:
    print("No")