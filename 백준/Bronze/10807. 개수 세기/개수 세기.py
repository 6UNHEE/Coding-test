while True:
    try:
        N = int(input())
        l = list(map(int, input().split()))
        a = int(input())
    except:
        break

    print(l.count(a))