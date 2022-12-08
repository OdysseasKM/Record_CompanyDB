import sqlite3


def menu():
    print( " Press 1 to add an artist \n Press 2 to add a release \n Press 3 to see all the artists \n Press 4 to see all the releases")
    choice = int(input())
    return choice

sql = ""
db = sqlite3.connect('record-company.db')
cursor = db.cursor()
print("ready")
choice=menu()

if choice == 1:
    idn = int(input("Give ID: "))
    nickname = input("Give Nickname: ")
    sql = """INSERT INTO ARTIST
    VALUES (?,?);"""
    cursor.execute(sql,(idn, nickname))

if choice == 2:
    artist_id = int(input("Give Artist ID: "))
    idn = int(input("Give ID: "))
    name = input("Give the name of the release: ")
    sql = """INSERT INTO RELEASE
    VALUES (?, ?, '8/12/2022', ?);"""
    cursor.execute(sql, (artist_id, idn, name))

if choice == 3:
    sql = """SELECT *
    FROM ARTIST;"""
    print(cursor.execute(sql).fetchall())
 
if choice == 4:
    sql = """SELECT *
    FROM RELEASE;"""
    print(cursor.execute(sql).fetchall())


db.commit()
print("done")
