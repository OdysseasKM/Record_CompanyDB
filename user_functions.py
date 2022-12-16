import sqlite3

def open_db():
    db = sqlite3.connect('database.db')
    global cursor
    cursor = db.cursor()


# 1. Τα 10 πιο δημοφιλή βίντεο (βάση views)
def querie1():
    sql = """select r.release_title, onl.views
        from release as r, video as v, format as f, online as onl
        where r.release_id = v.video_id and v.video_id = f.format_id and f.format_id = onl.id
        order by onl.views DESC
        limit 10;"""
    print(cursor.execute(sql).fetchall())

# 2. Τα 10 πιο δημοφιλή βίντεο συγκεκριμένου genre.
def querie2():
    print("genres:",end="")
    sql = """select GENRE.name
            from GENRE 
            GROUP by GENRE.name;"""
    print(cursor.execute(sql).fetchall())  
    genre = input("Type a genre : ") 
    sql = """select r.release_title , onl.views, g.name
            from release as r, video as v, format as f, online as onl, genre as g
            where r.release_id = v.video_id and 
            v.video_id = f.format_id and 
            f.format_id = g.rel_id and 
            f.format_id = onl.id and
			g.name = ?
            order by onl.views DESC
            limit(10)"""
    cursor.execute(sql, (genre,))
    result = cursor.fetchall()
    print(result)

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

# 8. Τα βίντεο ενός καλλιτέχνη.
def querie3():
    artist_id = int(find_artist_with_nickname())
    if (artist_id !=-1):
        sql = """select r.release_title
                FROM release as r, video as v, artist as a
                where a.id = r.artist_id and v.video_id = r.release_id and a.id = ?"""
        cursor.execute(sql,(artist_id,))
        result = cursor.fetchall()
        print(result)

def find_song_with_id(song_name = ""):
    if song_name == "": song_name = input("select song : ")
    id = int(input("type an id for song: "))
    sql = """select song.song_id, release.release_title
            from song join release on song_id = release_id
            where release_title = ? and release_id = ?"""
    cursor.execute(sql,(song_name,id))
    return id

def find_song():
    sql = """select song.song_id, release.release_title
            from song join release on song_id = release_id
            where release_title = ?"""
    song_name = input("select song : ")
    cursor.execute(sql,(song_name,))
    result = cursor.fetchall()
    if (len(result)==0):
        print("this song does not exist.")
        choice = int(input("if you want to try again type 1, or -1 to exit. select : "))
        if (choice==1): 
            id = find_song()
            return id
        elif (choice==-1): return -1
    elif (len(result)>1):
        print(result)
        print("found more than one song with this name.")
        id = find_song_with_id(song_name)
    else: id = result[0][0]
    return id

# 10. Επιλέγοντας ένα τραγούδι ή ενα άλμπουμ να εμφανίζονται στον χρήστη 5 προτεινόμενα τραγούδια η άλμπουμ (βασισμένα στο είδος και στο rating) 
def querie4():
    song_id = int(find_song())
    if (song_id!=-1):
        # find genre of song
        sql = """select genre.name 
                from song join genre on song.song_id = genre.rel_id
                where song_id = ? 
                limit (1);"""
        cursor.execute(sql,(song_id,))
        genre = cursor.fetchall()[0][0]
        sql = """select r.release_id, r.release_title, avg(rate.stars) as avg_stars
                from release as r, song as s, genre as g, RATING as rate
                where r.release_id = s.song_id AND
                s.song_id = g.rel_id and 
                rate.rel_id = g.rel_id and 
                g.name = ?  
                group by r.release_id 
                order by avg_stars DESC
                LIMIT (5);"""
    cursor.execute(sql,(genre,))
    result = cursor.fetchall()
    print(result)

# 4. Artist (ή Writer) με το καλύτερο μέσο όρο rating στα releases.
def querie5():
    sql = """select a.nickname, Round (avg(rate.stars), 2) as avg_rate
            from artist as a, release as r, RATING as rate
            where a.id = r.artist_id AND
            r.release_id = rate.rel_id
            group by artist_id
            order by avg_rate DESC"""
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
