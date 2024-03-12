# db1.py 
import sqlite3
#연결 인스턴스(메모리에서 연습) 
#con = sqlite3.connect(":memory:")
con = sqlite3.connect("c:\\work\\demo.db")

#커서 인스턴스(실제 구문 실행)
cur = con.cursor() 
#테이블 구조 생성
cur.execute("create table if not exists PhoneBook (name text, phoneNum text);")

#1건 데이터 입력
cur.execute("insert into PhoneBook values ('홍길동','010-222');")

#입력 파라메터 처리
name = "박문수"
phoneNum = "010-123"
cur.execute("insert into PhoneBook values (?, ?);", (name, phoneNum))

#여러건 입력 
datalist = (("tom","010-333"),("dsp","010-567"))
cur.executemany("insert into PhoneBook values (?, ?);", datalist)

#검색
cur.execute("select * from PhoneBook;")
for row in cur:
    print(row)

