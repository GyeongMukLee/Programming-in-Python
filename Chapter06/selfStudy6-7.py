i, k = 0, 0
shape = "\u2665"

i = 0
for i in range(9):
    if i < 5:
        for k in range(4-i):
            print(" ", end="")
            k += 1
        for k in range(i*2+1):
            print(shape, end="")
            k += 1
    else:
        for k in range(i-4):
            print(" ", end="")
            k += 1
        for k in range((9-i)*2-1):
            print(shape, end="")
            k += 1
    print()
    i += 1
