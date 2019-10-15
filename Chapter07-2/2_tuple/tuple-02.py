sampleTuple=(4,3,9,1,3,9,3,3)

print("\n4. 샘플 튜플에서 특정 값의 갯수 카운트(count)")
print("   sampleTuple= ", sampleTuple)
print("   sampleTuple.count(3) = ", sampleTuple.count(3))
print("   sampleTuple.count(9) = ", sampleTuple.count(9))
print("   sampleTuple.count(2) = ", sampleTuple.count(2))

print("\n5. 샘플 튜플의 정렬")
print("    sampleTuple= ", sampleTuple)
print("    print(sorted(sampleTuple)) = ", sorted(sampleTuple))
print("    sortedSampleTuple= sorted(sampleTuple) ")
sortedSampleTuple= sorted(sampleTuple)
print("    sortedSampleTuple= ",sortedSampleTuple)
print("    sampleTuple= ", sampleTuple)

# sort()는 변경불가능한 자료형에서 사용하지 못함. 다음은 AttributeError가 발생함
# print("    print(sampleTuple.sort()) = ", sampleTuple.sort())
# print("    sampleTuple= ", sampleTuple)
