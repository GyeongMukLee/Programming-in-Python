sampleSet1 = {1, 2, 3, 4}

print("\n3. 샘플 세트의 정렬: 세트 자료형은 정렬되어 유지되므로 의미 없음")
print("    sampleSet1 = ", sampleSet1)
print("    print(sorted(sampleSet1)) = ", sorted(sampleSet1))
print("    sortedSampleSet1 = sorted(sampleSet1) ")
sortedSampleSet1 = sorted(sampleSet1)
print("    sortedSampleSet1 = ", sortedSampleSet1)
print("    sampleSet1 = ", sampleSet1)


print("\n4. 샘플 세트를 이용한 Python스러운 Loop")
print("    sampleSet1 = ", sampleSet1)
total = 0
for i in sampleSet1:
    total += i

print("    total = 0\n    for iin sampleSet1:")
print("       total += i\n    print(total) = %s" % total)
