N, X = map(int, input().split())
l = list(map(int, input().split()))

for i in range(N):
    if l[i] < X :
        print(l[i], end=' ')