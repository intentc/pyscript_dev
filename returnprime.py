
def prime_numbers():
    lst = []
    for x in range(2, 100):
        for y in range(2,int(x/2) + 1):
            if (x % y == 0):
                lst.append(x)
    return [n for n in range(2, 100) if n not in lst]


print(prime_numbers())
