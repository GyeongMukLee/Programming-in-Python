sampleList = [4, 3, 9, 1, 3, 6, 3, 3]

print("\n9. 샘플리스트에 한 값의 제거(remove)")
print("   9-1. 샘플리스트에 한 값의 제거")
print("      sampleList= ", sampleList)
print("      sampleList.index(9) = ", sampleList.index(9))
sampleList.remove(9)
print("      sampleList.remove(9) 후의 sampleList= ", sampleList)

print("   9-2. 샘플리스트에 한 값의 제거(같은 값이 여러개가 있을경우)")
print("      sampleList= ", sampleList)
print("      sampleList.count(3) = ", sampleList.count(3))
print("      sampleList.index(3) = ", sampleList.index(3))
sampleList.remove(3)
print("      sampleList= ", sampleList)

print("\n10. 샘플리스트의 갯수 카운트( len(샘플리스트) )")
print("    sampleList= ", sampleList)
print("    len(sampleList) = ", len(sampleList))
