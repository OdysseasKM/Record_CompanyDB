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

CREATE TABLE ALBUM (
	album_id integer NOT NULL,
	a_name varchar NOT NULL,
	PRIMARY KEY (album_id),
	FOREIGN KEY (album_id)
	REFERENCES RELEASE(rel_id)
    ON DELETE CASCADE
);

CREATE TABLE VIDEO (
	video_id integer NOT NULL,
	duration time,
	PRIMARY KEY (video_id)
	FOREIGN KEY (video_id)
    REFERENCES RELEASE(rel_id)
    ON DELETE CASCADE
);


CREATE TABLE SONG (
	song_id integer NOT NULL,
	album_id integer,
	duration time,
	video_id time,
	studio_id integer,
	lyrics_language varchar,
	PRIMARY KEY (song_id),

	FOREIGN KEY (song_id)
    REFERENCES RELEASE(rel_id)
    ON DELETE CASCADE,

	FOREIGN KEY (album_id)
	REFERENCES ALBUM(album_id)
    ON DELETE CASCADE,

	FOREIGN KEY (video_id)
    REFERENCES VIDEO(video_id)
);


CREATE TABLE INDIVIDUAL (
	ssn varchar NOT NULL,
	artist_id integer,
	first_name varchar,
	last_name varchar,
	PRIMARY KEY (ssn),
	FOREIGN KEY (artist_id)
    REFERENCES ARTIST(artist_id)
);

CREATE TABLE STUDIO (
	studio_id integer NOT NULL,
	street varchar,
	number varchar,
	town varchar,
	country varchar,
	PRIMARY KEY (studio_id)
);

CREATE TABLE RATING (
	stars integer NOT NULL,
	rel_id integer NOT NULL,
	FOREIGN KEY (rel_id)
	REFERENCES RELEASE(rel_id)
    ON DELETE CASCADE
);


CREATE TABLE CONTRIBUTOR (
	last_name varchar,
	first_name varchar,
	ssn varchar NOT NULL,
	PRIMARY KEY (ssn)
);

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

CREATE TABLE FORMAT (
	rel_id integer NOT NULL,
	format_id integer NOT NULL,
	PRIMARY KEY (format_id),

	FOREIGN KEY (rel_id)
	REFERENCES RELEASE(rel_id)
    ON DELETE CASCADE
);

CREATE TABLE VYNIL (
	format_id integer NOT NULL, 
	sales integer,
	cost float,
	FOREIGN KEY (format_id)
	REFERENCES FORMAT(format_id)
	ON DELETE CASCADE
);

CREATE TABLE CD (
	format_id integer NOT NULL,
	sales integer,
	cost float,
	FOREIGN KEY (format_id)
	REFERENCES FORMAT(format_id)
	ON DELETE CASCADE
);

CREATE TABLE DIGITAL (
	format_id integer NOT NULL,
	views integer,
	FOREIGN KEY (format_id)
	REFERENCES FORMAT(format_id)
	ON DELETE CASCADE
);

















