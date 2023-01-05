import sqlite3
import datetime 

sql = ""
db = sqlite3.connect('record-company.db')
cursor = db.cursor()

def find_all(table):
    
    if table == "Artist":
        sql = """SELECT nickname, origin
        FROM ARTIST;"""
        return(cursor.execute(sql).fetchall())

    elif table == "Studio":
        sql = """SELECT studio_id, town
        FROM STUDIO;"""
        return(cursor.execute(sql).fetchall())
    
    elif table == "Release":
        sql = """SELECT release_title, nickname
        FROM RELEASE JOIN ARTIST ON artist_id = id;"""
        return(cursor.execute(sql).fetchall())

    elif table == "Contributor":
        sql = """SELECT ssn, first_name, last_name, role
        FROM CONTRIBUTOR JOIN CONTIBUTS_IN ON ssn=contributor_id;"""
        return(cursor.execute(sql).fetchall())
    
def add_artist(name, country):

    sql="""SELECT MAX(id)
    FROM ARTIST;"""
    max_id=cursor.execute(sql).fetchone()[0]
    max_id += 1

    sql = """INSERT INTO ARTIST
    VALUES(?, ?, ?);"""
    cursor.execute(sql,(max_id, name, country))
    db.commit()

    
def add_release(art_name, name, option, genre, language="", Format="", duration=100, song_id=0, cost=0, studio_id=0, song_name=""):

    date = datetime.date.today()
    sql="""SELECT MAX(rel_id)
    FROM RELEASE;"""
    max_id=cursor.execute(sql).fetchone()[0]
    max_id += 1

    sql = """SELECT id
    FROM ARTIST
    WHERE ARTIST.nickname= ?;"""
    artist_id = cursor.execute(sql, (art_name,)).fetchone()[0]

    if check_genre(genre)==0:
        add_genre(genre)

    sql = """SELECT g_id
    FROM GENRE
    WHERE GENRE.g_name= ?;"""
    genre_id = cursor.execute(sql, (genre,)).fetchone()[0]

    sql = """INSERT INTO RELEASE
    VALUES(?, ?, ?, ?, ?);"""
    cursor.execute(sql, (max_id, artist_id, date, name, genre_id))


    if option == "Album":
        add_album(max_id, name)
    elif option == "Video":
        add_video(max_id, song_name, duration)
    elif option == "Single":
        add_song(max_id, None, duration, studio_id, language, name)

    if Format == "Vinyl":
        add_format(max_id, 1, cost)
    elif Format == "CD":
        add_format(max_id, 2, cost)
    elif Format == "Digital":
        add_format(max_id, 3)


    db.commit()


def add_album(idn, name):

    sql="""INSERT INTO ALBUM
    VALUES(?, ?);"""
    cursor.execute(sql,(idn, name))

def add_video(idn, song_name, duration):

    sql = """SELECT song_id
    FROM SONG
    WHERE SONG.name= ?;"""
    song_id = cursor.execute(sql, (song_name,)).fetchone()[0]

    sql="""INSERT INTO VIDEO
    VALUES(?, ?, ?);"""
    cursor.execute(sql,(idn, song_id, duration))

def add_song(rel_id, album_name, duration, studio_id, language, name):

    sql="""SELECT MAX(song_id)
    FROM SONG;"""
    max_id=cursor.execute(sql).fetchone()[0]
    max_id += 1

    sql = """SELECT rel_id
    FROM RELEASE
    WHERE RELEASE.release_title= ?;"""
    album_id = cursor.execute(sql, (album_name,)).fetchone()[0]

    sql="""INSERT INTO SONG
    VALUES(?, ?, ?, ?, ?, ?, ?);"""
    cursor.execute(sql,(max_id, rel_id, album_id, duration, studio_id, language, name))
    db.commit()

def add_format(rel_id, option, cost=0):

    sql="""SELECT MAX(format_id)
    FROM FORMAT;"""
    FORMAT_id=cursor.execute(sql).fetchone()[0]
    FORMAT_id += 1

    sql="""INSERT INTO FORMAT
    VALUES(?,?);"""
    cursor.execute(sql,(rel_id, FORMAT_id))

    if option==1:
        add_vinyl(FORMAT_id, cost)
    elif option==2:
        add_cd(FORMAT_id, cost)
    elif option==3:
        add_digital(FORMAT_id)
    db.commit()


def add_vinyl(idn, cost):

    sql="""INSERT INTO VINYL
    VALUES(?, 0, ?);"""
    cursor.execute(sql,(idn, cost))

def add_cd(idn, cost):

    sql="""INSERT INTO CD
    VALUES(?, 0, ?);"""
    cursor.execute(sql,(idn, cost))

def add_digital(idn):

    sql="""INSERT INTO DIGITAL
    VALUES(?, 0);"""
    cursor.execute(sql,(idn,))

def add_contributor(release_name, ssn, fname, lname, role):

    sql = """SELECT rel_id
    FROM RELEASE
    WHERE RELEASE.release_title= ?;"""
    idn = cursor.execute(sql, (release_name,)).fetchone()[0]

    sql="""INSERT INTO CONTIBUTS_IN
    VALUES(?, ?, ?);"""
    cursor.execute(sql,(ssn, idn, role))

    sql="""SELECT *
        FROM CONTRIBUTOR
        WHERE ssn=?;"""
    cursor.execute(sql,(ssn,))
    result = cursor.fetchall()
    if len(result) == 0:
        sql="""INSERT INTO CONTRIBUTOR
        VALUES(?, ?, ?);"""
        cursor.execute(sql,(lname, fname, ssn))

    db.commit()

def add_genre(name):
    
    sql="""SELECT MAX(g_id)
    FROM GENRE;"""
    max_id=cursor.execute(sql).fetchone()[0]
    max_id += 1
    print(max_id)
    sql="""INSERT INTO GENRE
    VALUES(?, ?);"""
    cursor.execute(sql,(name, max_id))
    db.commit()
    print("added")

def add_publish(art_id, rel_id):

    sql="""INSERT INTO PUBLISH
    VALUES(?, ?);"""
    cursor.execute(sql,(art_id, rel_id))


def add_feature_in(art_id, rel_id):

    sql="""INSERT INTO FEATURE_IN
    VALUES(?, ?);"""
    cursor.execute(sql,(art_id, rel_id))

def check_contibutor(Ssn):

    sql="""SELECT *
        FROM CONTRIBUTOR
        WHERE Ssn=?;"""
    cursor.execute(sql,(Ssn,))
    result = cursor.fetchall()
    return (len(result))

def check_genre(g_name):

    sql="""SELECT *
        FROM GENRE
        WHERE g_name=?;"""
    cursor.execute(sql,(g_name,))
    result = cursor.fetchall()
    return (len(result))

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
    ORDER BY ESODA
    LIMIT 3;"""
    print(cursor.execute(sql,(name,)))
    
def studios():
    
    sql="""SELECT STUDIO.id, SUM(SONG.song_id) AS recordings
    FROM STUDIO JOIN SONG ON id=studio_id
    GROUP BY STUDIO.id
    ORDER BY recordings;"""
    return(cursor.execute(sql))

def delete_release(idn):

    sql="""DELETE FROM RELEASE
    WHERE rel_id=?;"""
    cursor.execute(sql,(idn,))
    db.commit()

def delete_artist(name):

    sql="""DELETE FROM ARTIST
    WHERE nickname=?;"""
    cursor.execute(sql,(name,))
    db.commit()

def add_studio(street, number, city, country):

    sql="""SELECT MAX(studio_id)
    FROM STUDIO;"""
    max_id=cursor.execute(sql).fetchone()[0]
    max_id += 1

    sql = """INSERT INTO STUDIO
    VALUES(?, ?, ?, ?, ?);"""
    cursor.execute(sql,(max_id, street, number, city, country))
    db.commit()

def add_individual(ssn, fname, lname, art_name):

    sql = """SELECT id
    FROM ARTIST
    WHERE ARTIST.nickname= ?;"""
    artist_id = cursor.execute(sql, (art_name,)).fetchone()[0]

    sql="""INSERT INTO INDIVIDUAL
    VALUES(?, ?, ?, ?);"""
    cursor.execute(sql,(ssn, artist_id, fname, lname))
    db.commit()






