def small_numbers(numbers, k):
    i = 0
    for x in numbers:
        if x < k:
            i += 1
    return i

print(small_numbers([6, 8, 10, 1, 24, 38], 7))

def pocitani(n):
    z = 1
    for y in range(1, 20):
        if y == 13:
            z += 1   
        else:
            print(z)
            z += 1

pocitani(20)


def pocitani_(b):
    for f in range(1, b):
        if f == 13:
            continue
        else:
            print(f)

pocitani_(16)
