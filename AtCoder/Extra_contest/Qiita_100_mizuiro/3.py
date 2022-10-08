s = input()

count = 0

def In_AGCT(S) -> bool:
    if 'A' == S or 'C' == S or 'G'== S or 'T' == S:
        
        return True
    return False

renzoku =0 
for i in s:

    if In_AGCT(i):
        renzoku += 1
        count = max(renzoku,count)
    else:
        renzoku = 0
print(count)