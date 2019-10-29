inStr = "<<<파<<이>>썬>>>"
outStr = str()

for i in inStr:
    if not (i == "<" or i == ">" or i == " "):
        outStr += i

print("원래 문자열 ==>", inStr)
print("바뀐 문자열 ==>", outStr)
