def isNumber(x: str) -> bool:
    """
    str타입의 문자열을 받아서 숫자이면 True를 반환하는 함수
    isdigit()메서드는 소수 형태의 문자열은 확인하지 않기 때문이다.
    """
    try:
        float(x)
    except:
        return False
    return True


def isNum_Alpha_Han(x: str) -> bool:
    if isNumber(x):
        # isdigit 메서드는
        # 소수 형태의 문자열은 확인하지 않기 때문이다.
        return "숫자입니다."
    elif x.isalpha():
        return "문자입니다."
    elif x.isalnum():
        return "문자+숫자입니다."
    else:
        return "모르겠습니다."


print(isNum_Alpha_Han("abcd123"))
