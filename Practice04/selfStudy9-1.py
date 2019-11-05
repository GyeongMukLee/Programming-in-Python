## 전역 변수 선언 부분 ##
coffee = 0


## 함수 선언 부분 ##
def coffee_machine(button):
    print()
    print("#1. (자동으로) 뜨거운 물을 준비한다.")
    print("#2. (자동으로) 종이컵을 준비한다.")

    if button == 1:
        print("#3. (자동으로) 아메리카노를 만든다.")
    elif button == 2:
        print("#3. (자동으로) 카페라떼를 만든다.")
    elif button == 3:
        print("#3. (자동으로) 카푸치노를 만든다.")
    elif button == 4:
        print("#3. (자동으로) 에스프레소를 만든다.")
    else:
        print("#3. (자동으로) 아무 커피나 만든다.")

    print("#4. (자동으로) 물을 붓는다.")
    print("#5. (자동으로) 스푼으로 젓는다.")
    print()


## 메인 코드 부분 ##
for customer in ["로제", "리사", "지수", "세나"]:
    coffee = int(input(customer + "님, 어떤 커피 드릴까요?(1:아메리카노, 2:카페라떼, 3:카푸치노, 4:에스프레소)"))
    coffee_machine(coffee)
    print(customer + "님~ 커피 여기 있습니다.")
