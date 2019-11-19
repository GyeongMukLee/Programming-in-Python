inputFileName = input("입력받을 파일명을 입력해주세요: ")
outFileName = input("출력할 파일명을 입력해주세요: ")

in_fp = open(inputFileName, mode="r", encoding="utf-8")
out_fp = open(outFileName, mode="w", encoding="utf-8")

for i in in_fp.readlines():
    out_fp.writelines(i)

in_fp.close()
out_fp.close()
print("====== 파일이 정상적으로 적용되었음 ======")