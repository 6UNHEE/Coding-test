o = [1, 1, 2, 2, 2, 8]

m = list(map(int, input().split()))

res = [ol - ml for ol, ml in zip(o, m)]

print(' '.join(map(str, res)))