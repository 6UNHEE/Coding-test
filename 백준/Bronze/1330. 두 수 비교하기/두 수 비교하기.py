while True:
    try:
        a, b = map(int, input().split())
    except:
        break

    if a > b:
        print(">")
    elif a < b:
        print("<")
    else:
        print("==")