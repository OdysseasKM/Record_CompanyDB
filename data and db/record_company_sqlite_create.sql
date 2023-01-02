DROP TABLE IF EXISTS ARTIST;
CREATE TABLE ARTIST (
	id integer NOT NULL,
	nickname varchar NOT NULL,
	origin varchar,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS GENRE;
CREATE TABLE GENRE (
	g_name varchar NOT NULL,
	g_id integer NOT NULL,
	PRIMARY KEY (g_id)
);

DROP TABLE IF EXISTS RELEASE;
CREATE TABLE RELEASE (
	rel_id integer NOT NULL,
	artist_id integer NOT NULL,
	r_date date,
	release_title varchar NOT NULL,
	genre_id integer,
	PRIMARY KEY (rel_id),

	FOREIGN KEY (artist_id)
	REFERENCES ARTIST(id)
    ON DELETE CASCADE

	FOREIGN KEY (genre_id)
	REFERENCES GENRE(g_id)
);

DROP TABLE IF EXISTS FEATURE_IN;
CREATE TABLE FEATURE_IN (
	artist_id integer NOT NULL,
	rel_id integer  NOT NULL,

	FOREIGN KEY (artist_id)
	REFERENCES ARTIST(id)
    ON DELETE CASCADE,

	FOREIGN KEY (rel_id)
	REFERENCES RELEASE(rel_id)
    ON DELETE CASCADE
);

DROP TABLE IF EXISTS ALBUM;
CREATE TABLE ALBUM (
	album_id integer NOT NULL,
	a_name varchar NOT NULL,
	PRIMARY KEY (album_id),
	FOREIGN KEY (album_id)
	REFERENCES RELEASE(rel_id)
    ON DELETE CASCADE
);


DROP TABLE IF EXISTS INDIVIDUAL;
CREATE TABLE INDIVIDUAL (
	ssn varchar NOT NULL,
	artist_id integer,
	first_name varchar,
	last_name varchar,
	PRIMARY KEY (ssn),
	FOREIGN KEY (artist_id)
    REFERENCES ARTIST(artist_id)
);

DROP TABLE IF EXISTS STUDIO;
CREATE TABLE STUDIO (
	studio_id integer NOT NULL,
	street varchar,
	number varchar,
	town varchar,
	country varchar,
	PRIMARY KEY (studio_id)
);

DROP TABLE IF EXISTS RATING;
CREATE TABLE RATING (
	stars integer NOT NULL,
	rel_id integer NOT NULL,
	FOREIGN KEY (rel_id)
	REFERENCES RELEASE(rel_id)
    ON DELETE CASCADE
);

DROP TABLE IF EXISTS CONTRIBUTOR;
CREATE TABLE CONTRIBUTOR (
	last_name varchar,
	first_name varchar,
	ssn varchar NOT NULL,
	PRIMARY KEY (ssn)
);

DROP TABLE IF EXISTS CONTIBUTS_IN;
CREATE TABLE CONTIBUTS_IN (
	contributor_id integer NOT NULL,
	rel_id integer NOT NULL,
	role varchar NOT NULL,

	FOREIGN KEY (rel_id)
	REFERENCES RELEASE(rel_id)
    ON DELETE CASCADE,

	FOREIGN KEY (contributor_id)
	REFERENCES CONTRIBUTOR(ssn)
    ON DELETE CASCADE
);

DROP TABLE IF EXISTS FORMAT;
CREATE TABLE FORMAT (
	rel_id integer NOT NULL,
	format_id integer NOT NULL,
	PRIMARY KEY (format_id),

	FOREIGN KEY (rel_id)
	REFERENCES RELEASE(rel_id)
    ON DELETE CASCADE
);

DROP TABLE IF EXISTS VINYL;
CREATE TABLE VYNIL (
	format_id integer NOT NULL, 
	sales integer,
	cost float,
	FOREIGN KEY (format_id)
	REFERENCES FORMAT(format_id)
	ON DELETE CASCADE
);

DROP TABLE IF EXISTS CD;
CREATE TABLE CD (
	format_id integer NOT NULL,
	sales integer,
	cost float,
	FOREIGN KEY (format_id)
	REFERENCES FORMAT(format_id)
	ON DELETE CASCADE
);

DROP TABLE IF EXISTS DIGITAL;
CREATE TABLE DIGITAL (
	format_id integer NOT NULL,
	views integer,
	FOREIGN KEY (format_id)
	REFERENCES FORMAT(format_id)
	ON DELETE CASCADE
);

DROP TABLE IF EXISTS VIDEO;
CREATE TABLE VIDEO (
    video_id integer NOT NULL,
    song_id integer NOT NULL,
    duration time,
    PRIMARY KEY (video_id)
    FOREIGN KEY (video_id)
    REFERENCES RELEASE(rel_id)
    ON DELETE CASCADE
    FOREIGN KEY (song_id)
    REFERENCES SONG(song_id)
);

DROP TABLE IF EXISTS SONG;
CREATE TABLE SONG (
    song_id integer NOT NULL,
    rel_id integer ,
    album_id integer,
    duration time,
    studio_id integer,
    lyrics_language varchar,
    title varchar,
    PRIMARY KEY (song_id),

    FOREIGN KEY (rel_id)
    REFERENCES RELEASE(rel_id)
    ON DELETE CASCADE,

    FOREIGN KEY (album_id)
    REFERENCES ALBUM(album_id)
    ON DELETE CASCADE
);
DROP TABLE IF EXISTS USER;
CREATE TABLE USER (
    username varchar NOT NULL,
    password varchar,
    is_admin boolean,
    PRIMARY KEY (username)
);
















