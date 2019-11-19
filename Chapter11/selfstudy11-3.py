fileName = input("파일명을 입력해주세요: ")
fp = open(fileName, mode="w", encoding="utf-8")

while True:
    fileContents = input("내용을 입력해주세요: ")
    if fileContents != "":
        fp.writelines(fileContents + "\n")
    else:
        break

fp.close()
print("======= 파일이 정상적으로 저장됨 ========")
