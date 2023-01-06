import sqlite3

def open_db():
    global cursor,db
    db = sqlite3.connect('record-company.db')
    cursor = db.cursor()

def commit_db():
    db.commit()

def close_db():
    db.commit()
    cursor.close()

def return_genre():
    sql = """select GENRE.g_name
            from GENRE 
            GROUP by GENRE.g_name
            order by GENRE.g_name"""
    return cursor.execute(sql).fetchall()

def find_artist_with_id(nickname = ""):
    if nickname == "": nickname = input("select artist (type nickname): ")
    id = int(input("type an id for artist: "))
    sql = """SELECT artist.nickname, artist.id
            FROM artist
            WHERE artist.nickname = ? and artist.id = ?"""
    cursor.execute(sql,(nickname,id))
    return id

def find_artist_with_nickname():
    sql = """SELECT artist.nickname, artist.id
            FROM artist
            WHERE artist.nickname = ?"""
    nickname = input("select artist : ")
    cursor.execute(sql,(nickname,))
    result = cursor.fetchall()
    if (len(result)==0):
        print("this artist does not exist.")
        choice = int(input("if you want to try again type 1, or -1 to exit. select : "))
        if (choice==1): 
            id = find_artist_with_nickname()
            return id
        elif (choice==-1): return -1
    elif (len(result)>1):
        print(result)
        print("found more than one artist with this nickaname.")
        id = find_artist_with_id(nickname)
    else: id = result[0][1]
    return id


def find_song(song_name):
    sql = """select song_id, title
            from song
            where title = ?"""
    cursor.execute(sql,(song_name,))
    result = cursor.fetchall()
    if (len(result)==0):return False
    return result[0][0]

def find_album(album_name):
    sql = """select album.album_id, release.release_title
            from album join release on album_id = rel_id
            where release_title = ?"""
    cursor.execute(sql,(album_name,))
    result = cursor.fetchall()
    if (len(result)==0):return False
    return result[0][0]

def find_video(album_name):
    sql = """select video.video_id, release.release_title
            from video join release on video_id = rel_id
            where release_title = ?"""
    cursor.execute(sql,(album_name,))
    result = cursor.fetchall()
    if (len(result)==0):return False
    return result[0][0]


def add_rating_for_song(id,stars):
    sql = """insert into rating (stars, song_id) values (?,?);"""
    cursor.execute(sql,(stars,id))

def add_rating_for_video(id,stars):
    sql = """insert into rating (stars, video_id) values (?,?);"""
    cursor.execute(sql,(stars,id))

# 1. Τα 10 πιο δημοφιλή βίντεο (βάση views)
def query1():
    sql = """select r.release_title, dig.views
        from release as r, video as v, format as f, digital as dig
        where r.rel_id = f.rel_id  and r.rel_id = v.video_id  and f.format_id = dig.format_id
        order by dig.views DESC"""
    return(cursor.execute(sql).fetchall())

# 2. Τα 10 πιο δημοφιλή βίντεο συγκεκριμένου genre.
def query2(genre):
    sql = """select r.release_title , dig.views
            from release as r join genre as g on r.genre_id=g.g_id, video as v, format as f, digital as dig
            where r.rel_id = v.video_id and
            r.rel_id = f.rel_id  and
			f.format_id = dig.format_id  and
			g.g_name = ?
            order by dig.views DESC"""
    cursor.execute(sql, (genre,))
    result = cursor.fetchall()
    return result

# 8. Τα βίντεο ενός καλλιτέχνη.
def query6():
    artist_id = int(find_artist_with_nickname())
    if (artist_id !=-1):
        sql = """select r.release_title
                FROM release as r, video as v, artist as a
                where a.id = r.artist_id and v.video_id = r.rel_id and a.id = ?"""
        cursor.execute(sql,(artist_id,))
        result = cursor.fetchall()
        print(result)

# 4. Artist με το καλύτερο μέσο όρο rating στα songs.
def query3():
    sql = """select a.nickname, Round (avg(rate.stars), 2) as avg_rate
                from artist as a, release as r, album as al, song as s, rating as rate
                where a.id = r.artist_id AND
                ((r.rel_id = al.album_id and s.album_id = al.album_id) or (r.rel_id = s.rel_id) ) AND
                s.song_id = rate.song_id 
                group by artist_id
                order by avg_rate DESC"""
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

# 10. Επιλέγοντας ένα τραγούδι ή ενα άλμπουμ να εμφανίζονται στον χρήστη 5 προτεινόμενα τραγούδια η άλμπουμ (βασισμένα στο είδος και στο rating) 
def query4(song_id):
    if (song_id!=-1):
        # find genre of song
        sql ="""select DISTINCT g.g_id, g.g_name, s.song_id
                from genre as g, song as s, release as r, album as al
                where ((r.rel_id = s.rel_id and r.genre_id = g.g_id) or 
				(r.rel_id = al.album_id and r.genre_id = r.genre_id and s.album_id = al.album_id)) AND
				s.song_id = ?"""
        cursor.execute(sql,(song_id,))
        genre = int(cursor.fetchall()[0][0])
        sql ="""select s.title, a.nickname, g.g_name, round ( avg(rate.stars) ,2 ) as avg_stars
            from artist as a, release as r, genre as g, song as s, album as al, RATING as rate
            where s.song_id!=? AND
			a.id = r.artist_id AND
			g.g_id = ? and r.genre_id = g.g_id AND
			((s.rel_id = r.rel_id) or (s.album_id = al.album_id and r.rel_id = al.album_id) ) AND
            rate.song_id = s.song_id 
            group by s.song_id
            order by avg_stars DESC
            """
        cursor.execute(sql,(song_id,genre))
        result = cursor.fetchall()
        return result

def query5():
    sql = """select s.title, a.nickname, round ( avg(rate.stars) ,2 ) as avg_stars
            from artist as a, release as r, song as s, album as al, RATING as rate
            where  
            a.id = r.artist_id and
            (s.rel_id = r.rel_id or (s.album_id = al.album_id and r.rel_id = al.album_id)) AND
            rate.song_id = s.song_id 
            group by s.song_id
            order by avg_stars DESC;"""
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def query6():
    sql = """select r.release_title, a.nickname, round ( avg(rate.stars) ,2 ) as avg_stars
            from artist as a, release as r, song as s, album as al, RATING as rate
            where  
            a.id = r.artist_id and
            r.rel_id = al.album_id  AND
			s.album_id = al.album_id and
            rate.song_id = s.song_id 
            group by s.album_id
            order by avg_stars DESC;"""
    cursor.execute(sql)
    result = cursor.fetchall()
    return result