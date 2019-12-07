import sqlite3 as sq

conn = sq.connect("TestDB")
cur1 = conn.cursor()
cur1.execute("DROP TABLE dept")
cur1.execute("CREATE TABLE dept(deptCode char(3),\
              deptName char(10),\
              loc char(1));")

cur1.execute("INSERT INTO dept VALUES('101', '컴공과', 'N');")
cur1.execute("INSERT INTO dept VALUES('102', '전자과', 'N');")
cur1.execute("INSERT INTO dept VALUES('101', '경영학과', 'P');")
cur1.execute("INSERT INTO dept VALUES('101', '화공과', 'N');")
conn.commit()
