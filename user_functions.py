import sqlite3

def open_db():
    db = sqlite3.connect('database.db')
    global cursor
    cursor = db.cursor()


# find 10 most viewed video clips 
def querie1():
    sql = """select r.release_title
        from release as r, video as v, format as f, online as onl
        where r.release_id = v.video_id and v.video_id = f.format_id and f.format_id = onl.id
        order by onl.views
        limit 10;"""
    print(cursor.execute(sql).fetchall())

# Τα 10 πιο δημοφιλή βίντεο συγκεκριμένου genre.
def querie2():
    open_db()
    sql = """select GENRE.name
            from GENRE 
            GROUP by GENRE.name;"""
    print(cursor.execute(sql).fetchall())   
    genre = input("Type a genre: ")
    


