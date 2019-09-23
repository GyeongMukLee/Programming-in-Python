def solution(a: int, b: int):
    '''
    2016년 1월 1일은 금요일이다.
    이 때 2016년 a월 b일은 무슨 요일인지 계산하는 함수
    '''

    day: list = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    month: list = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    sum = 0

    for i in range(1, a):
        sum += month[i]

    sum += b-1

    return day[sum % 7]


print(solution(5, 24))
