T = int(input())
for _ in range(T):
    R, S = input().split()
    NS = ''
    for i in range(len(S)):
        NS += S[i] * int(R)
    print(NS)