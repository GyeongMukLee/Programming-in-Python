li1 = []
li2 = []

for i in range(0, 4):
    for j in range(0, 5):
        li1.append((i*5+j)*3)
    li2.append(li1)
    li1 = []

for i in range(0, 4):
    for j in range(0, 5):
        print("%3d" % li2[i][j], end="")
    print("")
