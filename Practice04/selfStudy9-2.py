## 함수 선언 부분 ##
def calc(v1, v2, op):
    result = 0
    if op == '+':
        result = v1 + v2
    elif op == '-':
        result = v1 - v2
    elif op == '*':
        result = v1 * v2
    elif op == '/':
        result = v1 / v2
    elif op == '**':
        result = v1 ** v2

    return result


def formatCheck(v2: int, op: str) -> bool:
    if op not in {"+", "-", "*", "/", "**"}:
        print("연산자가 잘못되었습니다.")
        return False
    if op == "/" and v2 == 0:
        print("0으로 나눌 수 없습니다.")
        return False
    return True


## 전역 변수 선언 부분 ##
res = 0
var1, var2, operator = 0, 0, ""


## 메인 코드 부분 ##
var1 = int(input("첫 번째 수를 입력하세요 : "))
operator = input("계산을 입력하세요(+, -, *, /, **) : ")
var2 = int(input("두 번째 수를 입력하세요 : "))

if formatCheck(var2, operator):
    res = calc(var1, var2, operator)
    print("## 계산기 : %d %s %d = %d" % (var1, operator, var2, res))
