def sumFromBeginningToEnd(first: int, last: int, step: int) -> int:
    sum = 0
    for i in range(first, last+1, step):
        sum += i

    return sum


first = int(input("합계를 구할 배열의 첫 번째 숫자를 입력해주세요: "))
last = int(input("합계를 구할 배열의 마지막 숫자를 입력해 주세요: "))
step = int(input("합계를 구할 배열의 간격을 입력해주세요: "))

print(first, " + ", first+step, " + ... + ", last, " = ",
      sumFromBeginningToEnd(first, last, step))
