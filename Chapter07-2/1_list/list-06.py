sampleList = [4, 1, 3, 6, 3, 3]

print("\n11. 샘플리스트를 이용한 Loop")
print("   11-1. Python스러운 Loop")
print("       sampleList= ", sampleList)
total = 0
for i in sampleList:
    total += i

print("       total = 0\n       for iin sampleList:")
print("         total += i\n       print(total) = %s" % total)


print("   11-2. range(len()) 함수를 이용한 Loop")
print("       sampleList= ", sampleList)
total = 0
for i in range(len(sampleList)):
    total += sampleList[i]

print("       total = 0\n       for iin range(len(sampleList)):")
print("         total += sampleList[i]\n       print(total) = %s" % total)
