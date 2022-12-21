DROP TABLE IF EXISTS ARTIST;
CREATE TABLE IF NOT EXISTS ARTIST
(
	id integer NOT NULL,
	nickname varchar NOT NULL,
	country varchar,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS RELEASE;
CREATE TABLE IF NOT EXISTS RELEASE 
(
	artist_id integer NOT NULL,
	release_id integer NOT NULL,
	r_date date,
	release_title varchar,
	PRIMARY KEY (release_id)
);

DROP TABLE IF EXISTS FEATURE_IN;
CREATE TABLE IF NOT EXISTS FEATURE_IN 
(
	artist_id integer NOT NULL,
	rel_id integer NOT NULL,
	FOREIGN KEY (artist_id)
	REFERENCES ARTIST(id)
    ON DELETE CASCADE,
	FOREIGN KEY (rel_id)
	REFERENCES RELEASE(release_id)
    ON DELETE CASCADE
);

DROP TABLE IF EXISTS PUBLISH;
CREATE TABLE IF NOT EXISTS PUBLISH 
(
	artist_id integer NOT NULL,
	rel_id integer NOT NULL,
	FOREIGN KEY (artist_id)
	REFERENCES ARTIST(id)
    ON DELETE CASCADE,
	FOREIGN KEY (rel_id)
	REFERENCES RELEASE(release_id)
    ON DELETE CASCADE
);

DROP TABLE IF EXISTS ALBUM;
CREATE TABLE IF NOT EXISTS ALBUM 
(
	id integer NOT NULL,
	a_name varchar,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS SONG;
CREATE TABLE IF NOT EXISTS SONG
(
    song_id integer NOT NULL,
    album_id integer ,
    writer_ssn varchar,
    duration time,
    video_id integer ,
    studio_id integer,
    PRIMARY KEY (song_id),
    FOREIGN KEY (video_id)
    REFERENCES VIDEO(video_id)
    ON DELETE CASCADE,
    FOREIGN KEY (album_id)
    REFERENCES ALBUM(id)
    ON DELETE CASCADE,
    FOREIGN KEY (song_id)
    REFERENCES RELEASE(release_id)
    ON DELETE CASCADE,
    FOREIGN KEY (writer_Ssn)
    REFERENCES WRITER(Ssn)
    ON DELETE CASCADE
    FOREIGN KEY (studio_id)
    REFERENCES STUDIO(id)
    ON DELETE CASCADE
);

DROP TABLE IF EXISTS VIDEO;
CREATE TABLE IF NOT EXISTS VIDEO 
(
	video_id integer NOT NULL,
	duration time,
	PRIMARY KEY (video_id)
);


DROP TABLE IF EXISTS WRITER;
CREATE TABLE IF NOT EXISTS WRITER 
(
	Ssn varchar,
	first_name varchar,
	last_name varchar,
	PRIMARY KEY (Ssn)
);

DROP TABLE IF EXISTS STUDIO;
CREATE TABLE IF NOT EXISTS STUDIO
(
    id integer NOT NULL,
    street varchar,
    number varchar,
    town varchar,
    country varchar,
    PRIMARY KEY (id)
);


DROP TABLE IF EXISTS LYRICS;
CREATE TABLE IF NOT EXISTS LYRICS
(
	song_id integer NOT NULL,
	language varchar,
	l_text text,
	FOREIGN KEY (song_id)
	REFERENCES SONG(song_id)
    ON DELETE CASCADE
);

DROP TABLE IF EXISTS RATING;
CREATE TABLE IF NOT EXISTS RATING 
(
	stars integer ,
	rel_id integer NOT NULL,
	FOREIGN KEY (rel_id)
	REFERENCES RELEASE(release_id)
    ON DELETE CASCADE
);

DROP TABLE IF EXISTS GENRE;
CREATE TABLE IF NOT EXISTS GENRE 
(
	name varchar,
	rel_id integer NOT NULL,
	FOREIGN KEY (rel_id)
	REFERENCES RELEASE(release_id)
    ON DELETE CASCADE
);

DROP TABLE IF EXISTS FORMAT;
CREATE TABLE IF NOT EXISTS FORMAT
(	
	format_id integer NOT NULL,
	rel_id integer NOT NULL,
	PRIMARY KEY(format_id)
	FOREIGN KEY (rel_id)
	REFERENCES RELEASE(release_id)
    ON DELETE CASCADE
);

DROP TABLE IF EXISTS VINYL;
CREATE TABLE IF NOT EXISTS VINYL 
(
	id integer NOT NULL,
	sales integer,
	cost integer,
	FOREIGN KEY (id)
	REFERENCES FORMAT(format_id)
    ON DELETE CASCADE
);

DROP TABLE IF EXISTS CD;
CREATE TABLE IF NOT EXISTS CD
(
	id integer NOT NULL,
	sales integer,
	cost integer,
	FOREIGN KEY (id)
	REFERENCES FORMAT(format_id)
    ON DELETE CASCADE
);

DROP TABLE IF EXISTS ONLINE;
CREATE TABLE IF NOT EXISTS ONLINE 
(
	id integer NOT NULL,
	views integer,
	FOREIGN KEY (id)
	REFERENCES FORMAT(format_id)
    ON DELETE CASCADE
);














