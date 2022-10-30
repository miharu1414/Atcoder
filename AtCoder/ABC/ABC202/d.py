import itertools

a,b,k = map(int,input().split())
s  = ""
for i in range(a):
    s+='0'
for j in range(b):
    s+='1' 

st = set()
for it in itertools.permutations(s):
    st.add("".join(it))
    
before = 0
for S in sorted(st):
    # print(int(S,2)-before)
    # before = int(S,2)
    print(int(str(int(S,2)),10))
    print(S)
    

