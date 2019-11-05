## 전역 변수 선언 부분 ##
coffee = 0


## 함수 선언 부분 ##
def coffee_machine(button):
    print()
    print("#1. (자동으로) 뜨거운 물을 준비한다.")
    print("#2. (자동으로) 종이컵을 준비한다.")
    print("#3. (자동으로) 에스프레소를 추출한다.")

    buttonClick(button)
    print()

def buttonClick(n:int) -> None:
    d = {
        1:americano,
        2:cafelatte,
        3:cappuccino,
        4:espresso
    }

    if n not in d:
        return amu_coffee()
    else:
        d[n]()

def americano() -> None:
    print("#4. (자동으로) 물을 붓는다.")


def cafelatte() -> None:
    print("#4. (자동으로) 우유를 붓는다.")


def cappuccino() -> None:
    print("#4. (자동으로) 우유를 붓는다.")
    print("#5. (자동으로) 우유 거품을 붓는다.")

def espresso() -> None:
    pass

def amu_coffee() -> None:
    print("#4. (자동으로) 아무 커피나 만든다.")



## 메인 코드 부분 ##
for customer in ["로제", "리사", "지수", "세나"]:
    coffee = int(
        input(customer + "님, 어떤 커피 드릴까요?(1:아메리카노, 2:카페라떼, 3:카푸치노, 4:에스프레소)"))
    coffee_machine(coffee)
    print(customer + "님~ 커피 여기 있습니다.")
