sampleList = [4,3,9,1]

print("\n7. 샘플리스트에 또 다른 리스트를 붙이기(extend)")
print("   sampleList= ", sampleList)
sampleList.extend([3, 6])
print("   sampleList.extend([3, 6]) 후의sampleList= ", sampleList)
addList = [3, 3]
print("   addList= [3,3]")
sampleList.extend(addList)
print("   sampleList.extend(addList) 후의sampleList= ", sampleList)

print("\n8. 샘플리스트에서 특정 값의 갯수 카운트(count)")
print("   sampleList= ", sampleList)
print("   sampleList.count(3) = ", sampleList.count(3))
print("   sampleList.count(9) = ", sampleList.count(9))
print("   sampleList.count(2) = ", sampleList.count(2))
