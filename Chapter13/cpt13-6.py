import sqlite3 as sq

conn = sq.connect("TestDB")
cur1 = conn.cursor()

del_deptName = input("삭제할 학과를 입력해주세요: ")

cur1.execute("DELETE FROM dept WHERE deptName='"
             + del_deptName + "';")

print("삭제되었습니다.")
conn.commit()
