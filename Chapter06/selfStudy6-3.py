for i in range(9, 1, -1):
    print("#%2d단#" % i, end=" ")
print("", end="\n")

for i in range(1, 10):
    for j in range(9, 1, -1):
        print("%dX%d=%2d" % (j, i, i*j), end=" ")
    print("", end="\n")
