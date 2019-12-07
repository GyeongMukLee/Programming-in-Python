import sqlite3 as sq

conn = sq.connect("TestDB")
cur1 = conn.cursor()

new_deptCode = input("학과 코드를 입력해주세요: ")
new_deptName = input("학과 이름을 입력해주세요: ")
new_loc = input("학과의 위치를 입력해주세요: ")

cur1.execute("INSERT INTO dept VALUES('"
             + new_deptCode + "', '"
             + new_deptName + "', '"
             + new_loc + "'); ")
print("DB에 추가되었습니다.")
conn.commit()
