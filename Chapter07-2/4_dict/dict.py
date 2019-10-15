# 딕셔너리 실습 소스코드 - 1
print("1. 다음의 5가지 딕셔너리 초기화 방법은 동일")
print("asampleDic = \
    {\"홍길동\": 97, \"김판서\": 75, \"성춘향\": 83, \"이율곡\": 61}")
asampleDic = {"홍길동": 97, "김판서": 75, "성춘향": 83, "이율곡": 61}

print("bsampleDic = \
    dict(홍길동=97, 김판서=75, 성춘향=83, 이율곡=61)")
bsampleDic = dict(홍길동=97, 김판서=75, 성춘향=83, 이율곡=61)

print("csampleDic = \
    dict(zip([\"홍길동\", \"김판서\", \"성춘향\", \"이율곡\"], [97, 75, 83, 61]))")
csampleDic = dict(zip(["홍길동", "김판서", "성춘향", "이율곡"], [97, 75, 83, 61]))

print("dsampleDic = \
    dict([(\"김판서\", 75), (\"홍길동\", 97), (\"성춘향\", 83), (\"이율곡\", 61)])")
dsampleDic = dict([("김판서", 75), ("홍길동", 97), ("성춘향", 83), ("이율곡", 61)])

print("esampleDic = \
    dict({\"이율곡\": 61, \"성춘향\": 83, \"김판서\": 75, \"홍길동\": 97})")
esampleDic = dict({"이율곡": 61, "성춘향": 83, "김판서": 75, "홍길동": 97})

print()

print("if(asampleDic == bsampledic) ==", asampleDic == bsampleDic)
print("if(bsampleDic == csampledic) ==", bsampleDic == csampleDic)
print("if(csampleDic == dsampledic) ==", csampleDic == dsampleDic)
print("if(dsampleDic == esampledic) ==", dsampleDic == esampleDic)
print("if(esampleDic == asampledic) ==", esampleDic == asampleDic)


# 딕셔너리 실습 소스코드 - 2
print("\n2. 딕셔너리의 길이: len(sampleDic)")
sampleDic = {"홍길동": 97, "김판서": 75, "성춘향": 83, "이율곡": 61}
print("   len(sampleDic) = ", len(sampleDic))


print("\n3. 딕셔너리의 키로 값 조회: sampleDic[key]")
print("   3-1. 특정 키로 값 찾기: sampleDic[key]")
print("    sampleDic['홍길동'] = ", sampleDic["홍길동"])
print("    sampleDic['김판서'] = ", sampleDic["김판서"])
print("    sampleDic['성춘향'] = ", sampleDic["성춘향"])
print("    sampleDic['이율곡'] = ", sampleDic["이율곡"])


print("\n   3-2. 루프를 이용한 모든 키의 값 검색")
for k in sampleDic:
    print("    sampleDic['"+k+"'] = ", sampleDic[k])


print("\n4. 특정 아이템의 값 바꾸기: sampleDic[key] = value")
for k in sampleDic:
    print("    sampleDic['"+k+"'] = ", sampleDic[k])

print()
sampleDic['홍길동'] = 10
sampleDic['김판서'] = 20
sampleDic['성춘향'] = 30
sampleDic['이율곡'] = 40

for k in sampleDic:
    print("    sampleDic['"+k+"'] = ", sampleDic[k])


# 딕셔너리 실습 소스코드 - 3
print("\n5. 특정 키로 딕셔너리 아이템 삭제하기: del sampleDic[key]")
print("    sampleDic =", sampleDic, "\n    len(sampleDic) =", len(sampleDic))
print("    del sampleDic['김판서']")
del sampleDic["김판서"]
print("    sampleDic =", sampleDic, "\n    len(sampleDic) =", len(sampleDic))

print("\n6. 딕셔너리에 특정 키가 있는지 여부의 불리언 결과 출력")
print("    sampleDic =", sampleDic, "\n    len(sampleDic) =", len(sampleDic))
if "홍길동" in sampleDic:
    print("    홍길동 있음")
else:
    print("    홍길동 없음")

if "김판서" in sampleDic:
    print("    김판서 있음")
else:
    print("    김판서 없음")

for k in sampleDic:
    print("   ", k, "가 sampleDic에 있음:", k in sampleDic)


# 딕셔너리 실습 소스코드 - 4
print("\n7. 딕셔너리 아이템을 순회하는 루프 만들기: iter(sampleDic)")
print("\n    7-1. 파이썬스러운 반복: iter(sampleDic)")
sampleDic["김판서"] = 50

for k in iter(sampleDic):
    print("    "+k)

print("\n7-2. 7-1과 같지만 읽기 좋은 반복 표현:iter(sampleDic).keys()")
for k in iter(sampleDic.keys()):
    print("    "+k)

print("\n8. sampleDic.get(k,default)")
print("    sampleDic에 k가 있으면 sampleDic[k]를 반환하고, 아니면 default를 반환")
print("sampleDic =", sampleDic)
print()
for k in ["홍길동", '성춘향', "이율곡", "김판서", "이순신"]:
    print("   ", k, "은", sampleDic.get(k, "결시"))


# 딕셔너리 실습 소스코드 - 5
print("\n9. 샘플 딕셔너리의 아이템, 키, 값 출력")
print("\n    9-1. 샘플 딕셔너리의 요소(item) 출력")
print("        sampleDic.items():", sampleDic.items())
print("\n    9-2. 샘플 딕셔너리의 키 출력")
print("        sampleDic.keys():", sampleDic.keys())
print("\n9-3. 샘플딕셔너리의 값 출력")
print("        sampleDic.values():", sampleDic.values())

print("\n10.샘플딕셔너리의 제일 마지막 아이템 삭제")
print("\n    10-1. 샘플딕셔너리의 특정 키를 갖는 아이템 삭제: pop(키)")
print("        sampleDic =", sampleDic)
print("        sampleDic.pop('홍길동')")
sampleDic.pop("홍길동")
print("        sampleDic =", sampleDic)
print("\n    10-2. 샘플딕셔너리의 임의의 아이템 삭제: popitem()")
print("        sampleDic =", sampleDic)
print("        sampleDic.popitem()")
sampleDic.popitem()
print("sampleDic =", sampleDic)

print("\n11. 딕셔너리 아이템 지우기: sampleDic.clear()")
print("    sampleDic =", sampleDic)
print("    sampleDic.clear()")
sampleDic.clear()
print("    sampleDic =", sampleDic)

sampleDic = {
    "홍길동": 10,
    "김판서": 20,
    "성춘향": 30,
    "이율곡": 40
}

# 딕셔너리 실습 소스코드 - 6
print("\n12. 딕셔너리를 이용한 다양한 작업")
print("\n    12-1. 딕셔너리를 이용한 값의 평균 구하기")
print("        sampleDic =", sampleDic)
sum_ = 0

for k in sampleDic:
    sum_ += sampleDic[k]
print("        값 평균:", sum_/len(sampleDic))

print("\n    12-2. 딕셔너리의 키나 값을 리스트로 만들기")
print("        type(keys):", type(sampleDic.keys()))
print("        type(values):", type(sampleDic.values()))
print("        type(list(keys)):", type(list(sampleDic.keys())))
print("        type(list(values)):", type(list(sampleDic.values())))
print("\n        키(keys)를 리스트로 출력:", list(sampleDic.keys()))
print("        값(values)을 리스트로 출력:", list(sampleDic.values()))

print("\n    12-3. 키값을 기준으로 정렬")
print("    sampleDic =", sampleDic)
print("    키(이름의 오름차순)를 기준으로 정렬한 결과")
print("        (1)아이템 출력:", sorted(sampleDic.items()))
print("        (2)아이템의 리스트 출력:", sorted(sampleDic.items()))
print("        (3)키 출력:", sorted(sampleDic.keys()))
print("        (4)키의 리스트 출력:", sorted(sampleDic.keys()))
print("        (5)값 출력:", sorted(sampleDic.values()))
print("        (6)값의 리스트:", sorted(sampleDic.values()))

print("\n    12-4. 딕셔너리를 이용한 집합 연산")
A = sampleDic.keys()
B = {"홍길동", "이성계", "김판서"}

print("        A:", A)
print("        B:", B)

print("        A&B:", A & B)
print("        A^B:", A ^ B)
