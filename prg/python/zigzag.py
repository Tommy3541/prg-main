def zigzag(n):
    for f in range(1, n):
        if f % 2 == 0:
            print("  ", f)
        else:
            print(f)

zigzag(20)

def zigzag(n):
    for i in range(1, n):
        if i % 5 == 0 and i % 8 == 0:
            print("bum prask")
        elif i % 5 == 0:
            print("bum")
        elif i % 8 == 0:
            print("prask")
        else:
            print(i)

zigzag(80)
