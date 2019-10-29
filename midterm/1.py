# 한경대학교 컴퓨터공학과
# 2018250038 이경묵


def calculator(a: int, operator: str, b: int):
    """
    정수 두 개와 연산자 하나를 받으면 결과를 출력하는 함수입니다.
    """
    return {
        "+": lambda a, b: a+b,
        "-": lambda a, b: a-b,
        "*": lambda a, b: a*b,
        "/": lambda a, b: a/b
    }[operator](a, b)


def input_format_check(a: str, operator: str, b: str):
    return_val = True
    if not a.isdigit():
        print("[ERROR] 첫 번째로 입력받은 것이 정수가 아닙니다.", end="\n\n")
        return_val = False
    if not operator in {"+", "-", "*", "/"}:
        print("[ERROR] 연산자가 올바르지 않습니다.", end="\n\n")
        return_val = False
    if not b.isdigit():
        print("[ERROR] 세 번째로 입력받은 것이 정수가 아닙니다.", end="\n\n")
        return_val = False
    return return_val


# ======== 메인 코드 부분 ========
print("===========================")
print("2018250038 이경묵")
print("사칙연산 계산기 프로그램")
print("===========================")

print("========")
print("입력")
print("========")

a = 0
operator = 0
b = 0

while True:
    a = input("첫 번째 정수를 입력해 주세요: ")
    operator = input("연산자(+, -, *, /)중 하나를 입력해 주세요: ")
    b = input("두 번째 정수를 입력해 주세요: ")
    if input_format_check(a, operator, b):
        break


print("========")
print("출력")
print("========")
print("연산 결과:", calculator(int(a), operator, int(b)))
