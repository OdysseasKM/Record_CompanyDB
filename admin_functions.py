import sqlite3
import datetime 

sql = ""
db = sqlite3.connect('record-company.db')
cursor = db.cursor()

def find_all(table):
    
    if table == "Artist":
        sql = """SELECT *
        FROM ARTIST;"""
        print(cursor.execute(sql).fetchall())

    elif table == "Studio":
        sql = """SELECT *
        FROM STUDIO;"""
        print(cursor.execute(sql).fetchall())
    
    elif table == "Release":
        sql = """SELECT *
        FROM RELEASE;"""
        print(cursor.execute(sql).fetchall())
    
def add_artist(name, country):

    sql="""SELECT MAX(id)
    FROM ARTIST;"""
    max_id=cursor.execute(sql).fetchone()[0]
    max_id += 1

    sql = """INSERT INTO ARTIST
    VALUES(?, ?, ?);"""
    cursor.execute(sql,(max_id, name, country))
    db.commit()

    
def add_release(art_name, name, option, Format, duration=100, writer_ssn="11", cost=10, Fname="", Lname="", studio_id=0):

    date = datetime.today()
    sql="""SELECT MAX(release_id)
    FROM RELEASE;"""
    max_id=cursor.execute(sql).fetchone()[0]
    max_id += 1

    sql = """SELECT id
    FROM ARTIST
    WHERE ARTIST.nickname= ?;"""
    artist_id = cursor.execute(sql, (art_name,)).fetchone()[0]

    sql = """INSERT INTO RELEASE
    VALUES(?, ?, ?, ?);"""
    cursor.execute(sql,(artist_id, max_id, date, name))


    add_publish(artist_id, max_id)

    if option == "Album":
        add_album(max_id, name)
    elif option == "Video":
        add_video(max_id, duration)
    elif option == "Single":
        add_song(max_id, None, writer_ssn, duration, None, studio_id)
        if check_writer(writer_ssn)==0:
            add_writer(writer_ssn, Fname, Lname)


    add_format(max_id)
    if Format == "Vinyl":
        add_vinyl(max_id, cost)
    elif Format == "CD":
        add_cd(max_id, cost)
    elif Format == "Online":
        add_online(max_id)


    db.commit()


def add_album(idn, name):

    sql="""INSERT INTO ALBUM
    VALUES(?, ?);"""
    cursor.execute(sql,(idn, name))

def add_video(idn, duration):

    sql="""INSERT INTO VIDEO
    VALUES(?, ?);"""
    cursor.execute(sql,(idn, duration))

def add_song(idn, album_id, writer_ssn, duration, video_id, studio_id):

    sql="""INSERT INTO SONG
    VALUES(?, ?, ?, ?, ?, ?);"""
    cursor.execute(sql,(idn, album_id, writer_ssn, duration, video_id, studio_id))

def add_format(rel_id):
    
    sql="""SELECT MAX(format_id)
    FROM FORMAT;"""
    max_id=cursor.execute(sql).fetchone()[0]
    max_id += 1

    sql="""INSERT INTO FORMAT
    VALUES(?, ?);"""
    cursor.execute(sql,(max_id, rel_id))

def add_vinyl(idn, cost):

    sql="""INSERT INTO VINYL
    VALUES(?, 0, ?);"""
    cursor.execute(sql,(idn, cost))

def add_cd(idn, cost):

    sql="""INSERT INTO CD
    VALUES(?, 0, ?);"""
    cursor.execute(sql,(idn, cost))

def add_online(idn):

    sql="""INSERT INTO VINYL
    VALUES(?, 0);"""
    cursor.execute(sql,(idn,))

def add_writer(ssn, fname, lname):

    sql="""INSERT INTO WRITER
    VALUES(?, ?, ?);"""
    cursor.execute(sql,(ssn, fname, lname))

def add_publish(art_id, rel_id):

    sql="""INSERT INTO PUBLISH
    VALUES(?, ?);"""
    cursor.execute(sql,(art_id, rel_id))


def add_feature_in(art_id, rel_id):

    sql="""INSERT INTO FEATURE_IN
    VALUES(?, ?);"""
    cursor.execute(sql,(art_id, rel_id))

def check_writer(ssn):

    sql="""SELECT EXISTS(
        SELECT 1 
        FROM WRITER
        WHERE Ssn=?);"""
    return(cursor.execute(sql(ssn,)))

def annual_revenue(year):

    sql="""SELECT SUM(VINYL.cost*VINYL.sales)
    FROM VINYL JOIN FORMAT ON id=rel_id JOIN RELEASE ON rel_id=release_id
    WHERE strftime("%Y", RELEASE.r_date)=?;"""
    vinyl_profit = cursor.execute(sql,(year,))

    sql="""SELECT SUM(CD.cost*CD.sales)
    FROM CD JOIN FORMAT ON id=rel_id JOIN RELEASE ON rel_id=release_id
    WHERE strftime("%Y", RELEASE.r_date)=?;"""
    cd_profit = cursor.execute(sql,(year,))

    total_revenue = cd_profit + vinyl_profit
    return total_revenue

def artist_profit(name):

    sql="""SELECT SUM(VINYL.cost)+SUM(CD.cost) AS ESODA
    FROM ARTIST JOIN RELEASE ON ARTIST.id=artist_id JOIN FORMAT ON release_id=rel_id JOIN VINYL ON format_id=VINYL.id JOIN CD ON format_id=CD.id
    WHERE ARTIST.nickname=?
    GROUP BY ARTIST.nickname
    ORDER BY ESODA;"""
    print(cursor.execute(sql,(name,)))
    
def studios():
    
    sql="""SELECT STUDIO.id, SUM(SONG.song_id) AS recordings
    FROM STUDIO JOIN SONG ON id=studio_id
    GROUP BY STUDIO.id
    ORDER BY recordings;"""
    print(cursor.execute(sql))

def delete_release(idn):

    sql="""DELETE FROM RELEASE
    WHERE release_id=?;"""
    cursor.execute(sql,(idn,))