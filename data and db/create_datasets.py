import openpyxl
import random
import sqlite3
from datetime import datetime, timedelta

# source = '/Users/johnefthymiou/Documents/university/7th senester/database/project/Record_CompanyDB/data and db/artist-song-album.xlsx'
# source1 = '/Users/johnefthymiou/Documents/university/7th senester/database/project/Record_CompanyDB/data and db/add_data_in_db.sql'
source = r'C:\Users\Odysseas\Documents\vaseis\data and db\artist-song-album.xlsx'
source1 = r'C:\Users\Odysseas\Documents\vaseis\data and db\add_data_in_db.sql'
start = datetime(2000, 1, 1)
end = datetime(2022, 1, 1)

def open_excel_file():
    global wb,sheet
    # open files
    wb = openpyxl.load_workbook(source)
    sheet = wb["Sheet1"]

def open_db():
    global db,cursor
    db = sqlite3.connect('record-company.db')
    cursor = db.cursor()

def create_artist_ids():
    i=99
    cur_artist_name = " "
    for rowNum in range (2,sheet.max_row):
        artist_name = sheet.cell(row=rowNum, column=3).value
        
        if (cur_artist_name==artist_name):
            sheet.cell(row=rowNum, column=2).value = i
        else:
            i+=1
            sheet.cell(row=rowNum, column=2).value = i
            cur_artist_name = artist_name
        # print(artist_name)
    wb.save(source)
            
def artist_data():
    ids = []

    exists = False
    for rowNum in range (2,sheet.max_row):
        #find artist id from each comumn
        artist_id = sheet.cell(row=rowNum, column=2).value

        #check if id has already added in file
        for i in range(1,len(ids)+1):
            # check first from the end of the pinax
            if (ids[-i]==artist_id): 
                exists = True
                break
        
        if (exists==False):
            #new aritst
            nickname = sheet.cell(row=rowNum, column=3).value
            r = random.randint(1,35)
            country = sheet.cell(row=r, column = 5).value
            #print(str(artist_id)+ " "+ nickname+ " "+ country)
            sql = """INSERT INTO ARTIST
                        VALUES(?, ?, ?);"""
            cursor.execute(sql,(artist_id, nickname, country))
            db.commit()
            ids.append(artist_id)
        exists = False

def add_format(release_id,format_id,vinyl,cd,digital):
    sql = """INSERT INTO FORMAT VALUES(?, ?);"""
    cursor.execute(sql,(release_id,format_id))
     
    if (vinyl==True):
        sales = random.randint(10,10000)
        cost = random.random() * 100
        cost = round(cost,2)
        sql = """INSERT INTO VINYL VALUES(?, ?, ?);"""
        cursor.execute(sql,(format_id,sales,cost))
       
    if (cd==True):
        sales = random.randint(10,10000)
        cost = random.random() * 100
        cost = round(cost,2)
        sql = """INSERT INTO CD VALUES(?, ?, ?);"""
        cursor.execute(sql,(format_id,sales,cost))

    if (digital==True):
        views = random.randint(100,1000000) 
        sql = """INSERT INTO DIGITAL VALUES(?, ?);"""
        cursor.execute(sql,(format_id,views))
    db.commit()

def add_rating_for_song(song_id):
    for j in range(random.randint(1,5)):
        rate = random.randint(1,5)
        sql = """INSERT INTO RATING (stars,song_id) VALUES(?, ?);"""
        cursor.execute(sql,(rate,song_id))
        db.commit() 

def add_rating_for_video(video_id):
    for j in range(random.randint(1,5)):
        rate = random.randint(1,5)
        sql = """INSERT INTO RATING (stars,video_id) VALUES(?, ?);"""
        cursor.execute(sql,(rate,video_id))
        db.commit() 

def release_data():
    song_id=100
    release_id=100
    format_id=100
    languages = ["greek","english","spanish"]
    current_album = ""
    for rowNum in range (2,sheet.max_row):
        column2 = sheet.cell(row=rowNum, column=1).value
        if (column2=="single"):
            #add release
            artist_id = sheet.cell(row=rowNum, column=2).value
            single_name = sheet.cell(row=rowNum, column=4).value
            random_date = start + timedelta(days=random.randint(0, (end - start).days))
            genre_id = random.randint(0,11)

            sql = """INSERT INTO RELEASE
                    VALUES(?, ?, ?, ?, ?);"""
            cursor.execute(sql,(release_id, artist_id, random_date, single_name, genre_id))
            db.commit()     

            # add_single
            duration = random.randint(100,500)
            studio_id = random.randint(0,4)
            language = random.choice(languages)

            sql = """INSERT INTO SONG (song_id,rel_id,duration,studio_id,lyrics_language,title)
                    VALUES(?, ?, ?, ?, ?, ?);"""
            cursor.execute(sql,(song_id, release_id,duration, studio_id, language, single_name))
            db.commit()
            add_rating_for_song(song_id)
            add_format(release_id,format_id,True,True,True)
            format_id+=1
            release_id +=1
            
            # video
            has_video = random.randint(0,10)
            # nine out of ten singles have video
            if (has_video!=0):
                # single has a video
                # add video release
                random_date = start + timedelta(days=random.randint(0, (end - start).days))
                sql = """INSERT INTO RELEASE
                    VALUES(?, ?, ?, ?, ?);"""
                cursor.execute(sql,(release_id, artist_id, random_date, single_name+" (video clip)", genre_id))
                db.commit() 

                duration = random.randint(100,500)
                sql = """INSERT INTO VIDEO
                    VALUES(?, ?, ?);"""
                cursor.execute(sql,(release_id, song_id, duration))
                db.commit() 
                add_rating_for_video(release_id)
                add_format(release_id,format_id,False,False,True)
                format_id+=1
                release_id +=1
            song_id+=1

        else:
            # it is an album
            if (column2!=current_album):
                # add album as a release
                artist_id = sheet.cell(row=rowNum, column=2).value
                random_date = start + timedelta(days=random.randint(0, (end - start).days))
                genre_id = random.randint(0,11)

                sql = """INSERT INTO RELEASE
                        VALUES(?, ?, ?, ?, ?);"""
                cursor.execute(sql,(release_id, artist_id, random_date, column2, genre_id))
                
                sql = """INSERT INTO ALBUM
                        VALUES(?);"""
                cursor.execute(sql,(release_id,))
                db.commit()
                add_format(release_id,format_id,True,True,True)
                format_id+=1
                
                album_id = release_id
                release_id +=1
                current_album = column2
                language = random.choice(languages)

            # add song 
            duration = random.randint(100,500)
            studio_id = random.randint(0,4)
            song_title = sheet.cell(row=rowNum, column=4).value
            sql = """INSERT INTO SONG (song_id, album_id, duration,studio_id,lyrics_language,title)
                    VALUES(?, ?, ?, ?, ?, ?);"""
            cursor.execute(sql,(song_id,album_id,duration,studio_id,language,song_title))
            db.commit()
            add_rating_for_song(song_id)

            # video
            has_video = random.randint(0,5)
            # one out of five songs have video clip
            if (has_video==0):
                # single has a video
                # add video release
                random_date = start + timedelta(days=random.randint(0, (end - start).days))
                sql = """INSERT INTO RELEASE
                    VALUES(?, ?, ?, ?, ?);"""
                cursor.execute(sql,(release_id, artist_id, random_date, song_title+" (video clip)", genre_id))
                db.commit() 

                duration = random.randint(100,500)
                sql = """INSERT INTO VIDEO
                    VALUES(?, ?, ?);"""
                cursor.execute(sql,(release_id, song_id, duration))
                db.commit() 
                add_rating_for_video(release_id)
                add_format(release_id,format_id,False,False,True)
                format_id+=1
                release_id +=1
            song_id+=1

def read_data_from_sql():
    with open(source1, 'r') as file:
        # Read all the lines
        lines = file.readlines()
        # Print the lines
        for line in lines:
            if (line=='\n'):continue
            else:
                cursor.execute(line)
                db.commit()

def main():
    open_excel_file()
    open_db()
    # create_artist_ids()

    read_data_from_sql()
    
    artist_data()
    release_data()
    
    print("your datasets are ready for queries.")
    wb.close()

if __name__ == "__main__":main()
            
		
