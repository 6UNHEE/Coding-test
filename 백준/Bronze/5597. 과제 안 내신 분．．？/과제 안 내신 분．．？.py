l = [i for i in range(1,31)] # 학생 번호 

for j in range(28):
    n = int(input())
    if n in l:
       l.remove(n) 
print(f'{l[0]}\n{l[1]}')