import operator

fp = open("Chapter08/OnlyYesterday.dat")
text = fp.read()
rep_text = text.replace(" ", "").replace(",", "").replace("\'", "").\
    replace(".", "").replace("(", "").replace(")", "").lower()
frequency = dict()
fp.close()

for word in rep_text:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

result: list = sorted(
    frequency.items(), key=operator.itemgetter(1), reverse=True)

print("원문: ", text)
print("====================")
print("문자", "\t", "빈도수")
print("====================")

for i in result:
    print(i[0], "\t", i[1])
