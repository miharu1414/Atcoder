n = int(input())
S = input()
if '|' in S[:S.index('*')] and '|' in S[S.index('*')+1:]:
    print('in')
else:
    print('out')