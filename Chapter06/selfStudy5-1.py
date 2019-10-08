score = int(input("점수를 입력하세요 : "))

if score >= 90:
    print("A", end="")
else:
    if score >= 80:
        print("B", end="")
    else:
        if score >= 70:
            print("C", end="")
        else:
            if score >= 60:
                print("D", end="")
            else:
                print("F")

if score >= 60 and score % 10 >= 5:
    print("+")
elif score >= 60 and score % 10 < 5:
    print("0")

print("학점입니다.")
