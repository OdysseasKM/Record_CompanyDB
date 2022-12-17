import sqlite3


def menu():
    print( " Press 1 to add an artist \n Press 2 to add a release \n Press 3 to see all the artists \n Press 4 to see all the releases")
    choice = int(input())
    return choice

def pick(options):
    print("Please choose:")

    for idx, element in enumerate(options):
        print("{}) {}".format(idx + 1, element))

    i = input("Enter number: ")
    try:
        if 0 < int(i) <= len(options):
            return int(i) - 1
    except:
        pass
    return None


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
    artist_name = input("Give Artist Name: ")
    idn = int(input("Give ID: "))
    name = input("Give the name of the release: ")

    options = ["Album", "Video", "Single"]
    category = pick(options)

    options2 = ["Album", "Video", "Single"]
    format = pick(options2)
    

    sql = """SELECT id
    FROM ARTIST
    WHERE ARTIST.nickname= ?;"""
    artist_id= cursor.execute(sql, (artist_name,)).fetchone()[0]

    sql = """INSERT INTO RELEASE
    VALUES (?, ?, '8/12/2022', ?);"""
    cursor.execute(sql, (artist_id, idn, name))

    if category == 0:
        sql = """INSERT INTO ALBUM
        VALUES (?,?);"""
        cursor.execute(sql, (idn, name))

    elif category == 1:
        duration = int(input("Give duration: "))

        sql = """INSERT INTO VIDEO
        VALUES (?,?);"""
        cursor.execute(sql, (idn, duration))

    elif category == 2:
        duration = int(input("Give duration: "))
        writer_ssn = int(input("Give writer's Ssn: "))

        sql = """INSERT INTO SONG
        VALUES (?, ?, ?, ?);"""
        cursor.execute(sql, (idn, None, duration, None))
        sql = """INSERT INTO WRITER
        VALUES (?, 'John', 'Efthimiou');"""
        cursor.execute(sql, (writer_ssn,))



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

