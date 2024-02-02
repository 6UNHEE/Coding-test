while True:
    try:
        a, b = map(str, input().split())
    except:
        break

    a, b = a[::-1], b[::-1]

    if int(a) > int(b):
        print(a)
    else:
        print(b)