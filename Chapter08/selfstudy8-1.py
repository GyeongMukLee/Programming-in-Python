text = "파이썬은완전재미있어요"

for i in range(len(text)):
    if i % 2 == 0:
        print(text[i], end="")
    else:
        print("#", end="")
