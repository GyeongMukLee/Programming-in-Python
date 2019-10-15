sampleSet1 = {4, 3, 1, 2}
sampleSet2 = {2, 3, 4, 5, 6}
sampleSet3 = {1, 2}
sampleSet4 = {3, 4}

print("\n5. 샘플세트의 연산")
print("   sampleSet1 합집합 sampleSet2  ", sampleSet1.union(sampleSet2))
print("   sampleSet1 교집합 sampleSet2  ", sampleSet1.intersection(sampleSet2))
print("   sampleSet1 차집합 sampleSet2  ", sampleSet1.difference(sampleSet2))
print("   sampleSet1 대칭차집합 sampleSet2  ",
      sampleSet1.symmetric_difference(sampleSet2))
print("   sampleSet3이 sampleSet1의 부분집합?  ", sampleSet3.issubset(sampleSet1))
print("   sampleSet3이 sampleSet1의 상위집합?  ", sampleSet3.issuperset(sampleSet1))
print("   sampleSet3과 sampleSet4가 서로소?  ", sampleSet3.isdisjoint(sampleSet4))
