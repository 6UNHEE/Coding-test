s = input()

dic = {'ABC':3, 'DEF':4, 'GHI':5, 'JKL':6, 'MNO':7, 'PQRS':8, 'TUV':9, 'WXYZ':10}
cnt = 0

for i in s:
    for j in dic.keys():
        if i in j:
            cnt += dic[j]
print(cnt)