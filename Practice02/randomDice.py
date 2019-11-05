import random


def diceRoll(dice: list):
    """
    인수로 들어온 리스트를 1~6 사이의 무작위 채우는 함수
    """
    for i in range(len(dice)):
        dice[i] = random.randint(1, 6)


def isAllDiceHasSameNumber(dice: list) -> bool:
    """
    모든 주사위가 같은 숫자인지 확인하는 함수
    모든 주사위가 같은 숫자이면 True를 반환한다.
    """
    for i in range(len(dice)-1):
        if dice[i]-dice[i+1] != 0:
            return False
    return True


def isDiceHasContinuousNumber(dice: list) -> bool:
    """
    주사위 리스트가 연속적인 숫자를 가지고있는지 확인하는 함수
    주사위 리스트 안에 [1,2,3,4,5,6]을 포함하면 True를 반환한다.
    """
    for i in range(len(dice)-5):
        if dice[i] == 1 and dice[i+1] == 2 and dice[i+2] == 3 and \
           dice[i+3] == 4 and dice[i+4] == 5 and dice[i+5] == 6:
            return True
    return False


dice = [0, 0, 0, 0, 0, 0]  # 주사위
trial = 0

while True:
    trial += 1
    diceRoll(dice)
    if isAllDiceHasSameNumber(dice):
        print("시행 ", trial, "회에 모두 동일한 숫자가 나옴: ", dice)
    elif isDiceHasContinuousNumber(dice):
        print("시행 ", trial, "회에 연속된 숫자가 나옴: ", dice)
        break
