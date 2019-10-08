hap = 0

while True:

    first = input("더할 첫 번째 수를 입력해주세요: ")
    second = input("더할 두 번째 수를 입력해주세요: ")

    if (first == "$") or (second == "$"):
        break

    print("=======================")
    print(first, " + ", second, " = ", int(first)+int(second))
    print("=======================")

print("$를 입력하여 반복문을 탈출했습니다.")
