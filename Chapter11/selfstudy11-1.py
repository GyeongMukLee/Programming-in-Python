fp = open("./Chapter11/data1.txt", mode="r", encoding="utf-8")

lineNum: int = 1
while True:
    line: str = fp.readline()
    if line == "":
        break
    print("%3d : %s" % (lineNum, line), end="")
    lineNum += 1
