def Fibo(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibo(n - 1) + Fibo(n - 2)


## 메인 코드 부분 ##
i = int(input("피보나치 수열 n값을 입력해주세요: "))
print("Fib(", i, ")=", Fibo(i))
