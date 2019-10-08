aa = []
bb = []

for i in range(0, 200):
    aa.append(i*3)

for i in range(0, 200):
    bb.append(aa[199-i])

print("bb[0]에는", bb[0], "이, bb[199]에는", bb[199], "이 입력됩니다.")
