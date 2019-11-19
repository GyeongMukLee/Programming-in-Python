fp = open("./Chapter11/data1.txt", mode="r", encoding="utf-8")

lineNum: int = 1
for i in fp.readlines():
    print("%3d : %s" % (lineNum, i), end="")
    lineNum += 1
