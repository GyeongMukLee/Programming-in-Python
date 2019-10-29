# 한경대학교 컴퓨터공학과
# 2018250038 이경묵

phonebook = {"홍길동": "010-8765-4321"}


def main_menu():
    """
    작업 내용을 나열하고 할 일을 받는 함수
    """
    print("=========")
    print("메인 메뉴")
    print("=========")
    print("\tI(i)를 입력하면 새로운 주소를 추가합니다.")
    print("\tD(d)를 입력하면 기존 주소 중 하나를 삭제합니다.")
    print("\tU(u)를 입력하면 기존 주소 중 하나의 전화번호를 변경합니다.")
    print("\tR(r)을 입력하면 주소록을 조회합니다.")
    print("\tQ(q)를 입력하면 주소록 프로그램을 종료합니다.", end="\n\n")

    return input("작업을 선택해주세요: ")


def select_menu(i: str):
    """
    메뉴를 선택하는 함수.

    프로그램을 종료하지 않고 유지할 경우 반환값은 True가 된다.
    """
    menu = {
        "I": phonebook_add,
        "D": phonebook_delete,
        "U": phonebook_change,
        "R": phonebook_lookup,
        "Q": phonebook_quit,
    }
    if i.upper() in menu:
        return menu[i.upper()]()
    else:
        return wrong_input()


def phonebook_add():
    name = input("주소록의 추가할 사람의 이름을 입력해주세요: ")
    if name in phonebook:
        print("해당 이름은 이미 등록되어 있습니다.", end="\n\n")
        return True

    number = input("전화번호를 입력해주세요:")
    phonebook[name] = number
    print("전화번호가 추가되었습니다.", end="\n\n")
    return True


def phonebook_delete():
    name = input("삭제할 사람의 이름을 입력해주세요: ")
    if not(name in phonebook):
        print("존재하지 않는 이름입니다.")
        return True

    if confirm("삭제"):
        phonebook.pop(name)
        print("삭제되었습니다.", end="\n\n")
    else:
        print("삭제하지 않았습니다.", end="\n\n")
    return True


def phonebook_change():
    name = input("전화번호를 변경할 사람의 이름을 입력해주세요: ")

    if not(name in phonebook):
        print("존재하지 않는 이름입니다.")
        return True

    if confirm("변경"):
        number = input("변경할 전화번호를 입력해주세요: ")
        phonebook[name] = number
        print("전화번호가 변경되었습니다.", end="\n\n")
    else:
        print("변경하지 않았습니다.", end="\n\n")
    return True


def phonebook_lookup():
    print("============================")
    print("주소록")
    print("%-4s  %15s" % ("이름", "전화번호"))
    print("============================")
    for i in phonebook:
        print("%-6s  %15s" % (i, phonebook[i]))
    print()
    return True


def phonebook_quit():
    if confirm("종료"):
        print("주소록 프로그램을 종료합니다. 이용해주셔서 감사합니다.")
        return False
    return True


def wrong_input():
    print("잘못 입력하셨습니다.", end="\n\n")
    return True


def confirm(ch: str):
    """
    사용자로부터 어떤 명령을 실행할것인지 확인하는 함수.
    Y(y)를 입력받으면 실행한다(True).
    """
    if "Y" == input("정말 "+ch+"하시겠습니까? "+ch+"하려면 Y(y)를 입력해주세요 ").upper():
        return True
    else:
        return False


# ======== 메인 코드 부분 ========
print("===========================")
print("2018250038 이경묵")
print("주소록 프로그램")
print("===========================", end="\n\n")

while True:
    if select_menu(main_menu()):
        continue
    break
