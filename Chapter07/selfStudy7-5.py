animal = {
    "닭": "병아리",
    "개": "강아지",
    "곰": "능소니",
    "고등어": "고도리",
    "명태": "노가리",
    "말": "망아지",
    "호랑이": "개호주"
}

while True:
    inputAnimal = input(str(list(animal.keys()))+"중 새끼이름을 알고싶은 동물은?: ")
    if inputAnimal in animal:
        print("<%s>의 새끼는 <%s>입니다." % (inputAnimal, animal.get(inputAnimal)))
    elif inputAnimal == "끝":
        break
    else:
        print("그런 동물이 없습니다. 확인해 보세요.")
