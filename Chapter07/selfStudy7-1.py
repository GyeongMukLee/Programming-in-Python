li = []
hap = 0

for i in range(0, 10):
    li.append(int(input(str(i+1)+"번째 숫자: ")))

i = 0

while i < 10:
    hap += li[i]
    i += 1


print("합계: ", hap)
