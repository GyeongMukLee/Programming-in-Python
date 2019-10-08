hap = 0
first = int(input("배열의 시작값을 입력해주세요: "))
last = int(input("배열의 마지막값을 입력해주세요: "))
step = int(input("배열 사이의 거리를 입력해주세요: "))
i = first

while i <= last:
    hap += i
    i += step

print("%d에서 %d까지 %d씩 증가시킨 값의 합계: %d" % (first, last, step, hap))
