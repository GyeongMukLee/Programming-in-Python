## 모듈 import 부분 ##
import datetime

## 함수 선언 부분 ##


def dateCalc(past: datetime.date, future: datetime.date) -> int:

    return_val = str(future-past).replace("days, 0:00:00", "")
    return int(return_val)


def dateParse(date: str) -> datetime.date:
    """
    YYYY/MM/DD 형태의 문자열을 date 객체로 변환하는 함수
    """
    year, month, day = map(int, date.split("/"))
    return datetime.date(year, month, day)


def dateOfThisYear(date: datetime.date) -> datetime.date:
    """
    날짜를 입력받으면 올해의 날짜를 반환하는 함수
    """
    return datetime.date(datetime.date.today().year,
                         date.month,
                         date.day)


def dateOfNextYear(date: datetime.date) -> datetime.date:
    """
    날짜를 입력받으면 내년의 날짜를 반환하는 함수
    """
    return datetime.date(datetime.date.today().year+1,
                         date.month,
                         date.day)


def isPassed(date: datetime.date) -> bool:
    """
    입력받은 날짜가 지났는지 확인하는 함수
    """
    if dateCalc(datetime.date.today(), date) <= 0:
        return True
    else:
        return False


def week(date: datetime.date) -> str:
    """
    날짜를 입력받으면 요일을 반환하는 함수
    """
    return ["월", "화", "수", "목", "금", "토", "일"][date.weekday()]


## 메인 코드 부분 ##
if __name__ == '__main__':
    birthday = input("출생일(년/월/일)을 입력해주세요: ")
    print("출생일 (", dateParse(birthday), ") 부터 오늘(", datetime.date.today(),
          ") 까지는", dateCalc(dateParse(birthday), datetime.date.today()), "일 지났습니다.")

    if isPassed(dateOfThisYear(dateParse(birthday))):
        print("내년 생일은", dateOfNextYear(dateParse(birthday)), "이고,",
              week(dateOfNextYear(dateParse(birthday))), "요일 입니다.")
    else:
        print("올해 생일은", dateOfThisYear(dateParse(birthday)), "이고,",
              week(dateOfThisYear(dateParse(birthday))), "요일 입니다.")
