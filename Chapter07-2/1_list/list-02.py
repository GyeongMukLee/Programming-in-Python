sampleList = [3, 4, 1]

print("\n4. 샘플 리스트의 정렬 3가지 방법")
print(" 4-1. 거꾸로 정렬 (reverse)")
print(" sampleList = ", sampleList)
sampleList.reverse()
print(" sampleList.reverse() 후의 sampleList = ", sampleList)

print(" 4-2. 오름차순으로 정렬")
print(" sampleList = ", sampleList)
sampleList.sort()
print(" sampleList.sort() 후의 sampleList = ", sampleList)

print(" 4-3. 내림차순으로 정렬")
print(" sampleList = ", sampleList)
sampleList.sort(reverse=True)
print(" sampleList.sort(reverse = True) 후의 sampleList = ", sampleList)
