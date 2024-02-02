while True:
    try:
        l = []
        for i in range(10):
            n = int(input())
            if (n % 42) not in l:
                l.append(n % 42)
    except:
        break
    print(len(l))