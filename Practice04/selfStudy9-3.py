## 함수 선언 부분 ##
def para_func(*args):
    return_val = 0
    for i in args:
        return_val += i
    return return_val


## 전역 변수 선언 부분 ##
hap = 0


## 메인 코드 부분 ##
hap = para_func(10, 20)
print("매개변수가 2개인 함수를 호출한 결과 ==> %d" % hap)
hap = para_func(10, 20, 30)
print("매개변수가 3개인 함수를 호출한 결과 ==> %d" % hap)