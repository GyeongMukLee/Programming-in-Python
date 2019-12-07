import sqlite3 as sq

conn = sq.connect("TestDB")
cur1 = conn.cursor()

find_loc = input("확인할 건물 코드를 입력해주세요: ")

cur1.execute("SELECT * FROM dept WHERE loc='"\
    + find_loc + "';")
i = cur1.fetchone()

while i:
    print("%4s  %12s  %2s" % (i[0], i[1], i[2]))
    i = cur1.fetchone()

conn.commit()
