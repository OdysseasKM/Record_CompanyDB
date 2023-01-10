import sqlite3
import datetime 

def open_db():
    global db,cursor
    db = sqlite3.connect('record-company.db')
    cursor = db.cursor()

def find_all(table):
    
    if table == "Bands":
        sql = """sELECT ARTIST.id,nickname, origin,COUNT(INDIVIDUAL.ssn)
        FROM ARTIST JOIN INDIVIDUAL ON ARTIST.id=INDIVIDUAL.artist_id
        GROUP BY ARTIST.id
        HAVING COUNT(INDIVIDUAL.ssn)>1;"""
        return(cursor.execute(sql).fetchall())

    if table == "Solo Artists":
        sql = """SELECT ARTIST.id, nickname, origin
        FROM ARTIST JOIN INDIVIDUAL ON ARTIST.id=INDIVIDUAL.artist_id
        GROUP BY ARTIST.id
        HAVING COUNT(INDIVIDUAL.ssn)<2;"""
        return(cursor.execute(sql).fetchall())

    elif table == "Studio":
        sql = """SELECT *
        FROM STUDIO;"""
        return(cursor.execute(sql).fetchall())
    
    elif table == "Release":
        sql = """SELECT release_title, nickname
        FROM RELEASE JOIN ARTIST ON artist_id = id;"""
        return(cursor.execute(sql).fetchall())

    elif table == "Contributor":
        sql = """sELECT ssn, first_name, last_name, rel_id,role
                FROM CONTRIBUTOR JOIN CONTRIBUTES_IN ON ssn=contributor_id;"""
        return(cursor.execute(sql).fetchall())

    elif table == "Albums":
        sql="""SELECT r.rel_id, r.release_title, a.nickname, ROUND(AVG(rate.stars), 2) AS avg_stars, COUNT(DISTINCT s.song_id)
                FROM artist AS a
                JOIN release AS r ON a.id = r.artist_id
                JOIN album AS al ON r.rel_id = al.album_id
                JOIN song AS s ON s.album_id = al.album_id
                LEFT JOIN RATING AS rate ON rate.song_id = s.song_id
                GROUP BY s.album_id
                ORDER BY avg_stars DESC;"""
        return(cursor.execute(sql).fetchall())

    elif table == "Songs":
        sql="""select distinct s.song_id, s.title, a.nickname, round ( avg(rate.stars) ,2 ) as avg_stars, s.album_id
            FROM artist AS a
			JOIN release AS r ON a.id = r.artist_id
			JOIN song AS s ON s.rel_id = r.rel_id OR (s.album_id = al.album_id AND r.rel_id = al.album_id)
			LEFT JOIN album AS al ON s.album_id = al.album_id
			LEFT JOIN RATING AS rate ON rate.song_id = s.song_id
            where  
            a.id = r.artist_id and
            (s.rel_id = r.rel_id or (s.album_id = al.album_id and r.rel_id = al.album_id)) 
            group by s.song_id
            order by avg_stars DESC;"""
        return(cursor.execute(sql).fetchall())

    elif table == "Videos":
        sql="""SELECT r.rel_id, r.release_title, ar.nickname, dig.views, ROUND(AVG(rate.stars), 2) AS avg_rate
            FROM release AS r
            JOIN artist AS ar ON ar.id = r.artist_id
            JOIN format AS f ON r.rel_id = f.rel_id
            JOIN digital AS dig ON f.format_id = dig.format_id
            JOIN video AS v ON r.rel_id = v.video_id
            LEFT JOIN rating AS rate ON rate.video_id = r.rel_id
            GROUP BY v.video_id
            ORDER BY dig.views DESC;
         """
        return(cursor.execute(sql).fetchall())
    
    elif table == "Individual":
        sql= """select i.ssn, i.first_name, i.last_name, ar.nickname
        from INDIVIDUAL  as i, artist as ar
        where ar.id = i.artist_id
        """
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

    if (genre!=""):
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
        add_album(max_id)
    elif option == "Video":
        add_video(max_id, song_name, duration)
    elif option == "Single":
        add_single(max_id, duration, studio_id, language, name)

    if Format == "Vinyl":
        add_format(max_id, 1, cost)
    elif Format == "CD":
        add_format(max_id, 2, cost)
    elif Format == "Digital":
        add_format(max_id, 3)
    db.commit()


def add_album(idn):
    sql="""INSERT INTO ALBUM
    VALUES(?);"""
    cursor.execute(sql,(idn,))

def add_video(idn, song_name, duration):
    sql = """SELECT song_id
    FROM SONG
    WHERE SONG.title= ?;"""
    song_id = cursor.execute(sql, (song_name,)).fetchone()[0]

    sql="""INSERT INTO VIDEO
    VALUES(?, ?, ?);"""
    cursor.execute(sql,(idn, song_id, duration))
    db.commit()

def add_single(rel_id, duration, studio_id, language, name):
    sql="""SELECT MAX(song_id)
    FROM SONG;"""
    max_id=cursor.execute(sql).fetchone()[0]
    max_id += 1

    sql="""INSERT INTO SONG
    VALUES(?, ?, ?, ?, ?, ?, ?);"""
    cursor.execute(sql,(max_id, rel_id, None, duration, studio_id, language, name))
    db.commit()

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

def add_contributor(ssn,rel_id,role):

    sql="""INSERT INTO CONTRIBUTES_IN (contributor_id,rel_id,role) VALUES(?, ?, ?);"""
    cursor.execute(sql,(ssn, int(rel_id), role))
    db.commit()

def add_contributor_as_person(ssn, fname, lname):
    sql = """INSERT into CONTRIBUTOR (last_name, first_name, ssn) values (?,?,?);"""
    cursor.execute(sql,(lname,fname,ssn))
    db.commit()
    

def add_genre(name):
    
    sql="""SELECT MAX(g_id)
    FROM GENRE;"""
    max_id=cursor.execute(sql).fetchone()[0]
    max_id += 1
    
    sql="""INSERT INTO GENRE
    VALUES(?, ?);"""
    cursor.execute(sql,(name, max_id))
    db.commit()
    

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

def sales():
    sql = """SELECT r.release_title, SUM(v.sales + c.sales) as sales
    FROM vinyl as v, cd as c, format as f, release as r
    where r.rel_id = f.rel_id AND
    v.format_id = f.format_id AND
    c.format_id = f.format_id 
    group by r.rel_id
    order by sales DESC
    limit 10;"""
    return(cursor.execute(sql).fetchall())

def artist_profit():

    sql="""SELECT ARTIST.nickname, round(SUM(VINYL.cost)+SUM(CD.cost),2) AS ESODA
    FROM ARTIST JOIN RELEASE ON ARTIST.id=RELEASE.artist_id JOIN FORMAT ON RELEASE.rel_id=FORMAT.rel_id JOIN VINYL ON FORMAT.format_id=VINYL.format_id JOIN CD ON FORMAT.format_id=CD.format_id
    GROUP BY ARTIST.nickname
    ORDER BY ESODA DESC"""
    return(cursor.execute(sql).fetchall())
    
def studios():
    
    sql="""SELECT STUDIO.studio_id, COUNT(SONG.song_id) AS recordings
    FROM STUDIO JOIN SONG ON STUDIO.studio_id=SONG.studio_id
    GROUP BY STUDIO.studio_id
    ORDER BY recordings DESC;"""
    return(cursor.execute(sql).fetchall())

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

def find_artist(name):
    sql = """
        select *
        from ARTIST as a
        where a.nickname = ?"""
    cursor.execute(sql,(name,))
    result = cursor.fetchall()
    if (len(result)==0):return False
    return True

def find_release(id):
    sql = """
        select *
        from RELEASE 
        where rel_id = ?"""
    cursor.execute(sql,(id,))
    result = cursor.fetchall()
    if (len(result)==0):return False
    return True