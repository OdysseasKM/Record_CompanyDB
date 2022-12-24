insert into ARTIST (id,nickname,origin) values (1, "john", "greece");
insert into ARTIST (id,nickname,origin) values (2, "ody", "greece");
insert into ARTIST (id,nickname,origin) values (3, "john the great", "greece");
insert into ARTIST (id,nickname,origin) values (4, "demitria", "albania");

INSERT into GENRE(g_name, g_id) values ('pop',1);
INSERT into GENRE(g_name, g_id) values ('indie, rock',2);
INSERT into GENRE(g_name, g_id) values ('indie',3);
INSERT into GENRE(g_name, g_id) values ('punk',4);

insert into RELEASE (artist_id, rel_id, r_date, release_title, genre_id) values (1, 1, "10/10/2000", "new release", 1);
insert into RELEASE (artist_id, rel_id, r_date, release_title, genre_id) values (1, 2, "10/10/2000", "new release1", 1);
insert into RELEASE (artist_id, rel_id, r_date, release_title, genre_id) values (1, 3, "10/10/2000", "new release2", 1);
insert into RELEASE (artist_id, rel_id, r_date, release_title, genre_id) values (2, 4, "10/10/2000", "new release3", 4);
insert into RELEASE (artist_id, rel_id, r_date, release_title, genre_id) values (2, 5, "10/10/2000", "new release4", 2);
insert into RELEASE (artist_id, rel_id, r_date, release_title, genre_id) values (2, 6, "10/10/2000", "new release5", 1);
insert into RELEASE (artist_id, rel_id, r_date, release_title, genre_id) values (3, 7, "10/10/2000", "new release6", 3);
insert into RELEASE (artist_id, rel_id, r_date, release_title, genre_id) values (3, 8, "10/10/2000", "new release7", 1);
insert into RELEASE (artist_id, rel_id, r_date, release_title, genre_id) values (3, 9, "10/10/2000", "new release8", 2);
insert into RELEASE (artist_id, rel_id, r_date, release_title, genre_id) values (3, 10, "10/10/2000", "new release8", 1);
insert into RELEASE (artist_id, rel_id, r_date, release_title, genre_id) values (4, 11, "10/10/2000", "kapsoura 8 mwromou", 2);
insert into RELEASE (artist_id, rel_id, r_date, release_title, genre_id) values (4, 12, "10/10/2000", "stepbrother i am stuck / hot mommy milker mom", 3);

insert into SONG (song_id) values (6);
insert into SONG (song_id) values (7);
insert into SONG (song_id) values (8);
insert into SONG (song_id) values (9);
insert into SONG (song_id) values (10);
insert into SONG (song_id) values (11);


insert into VIDEO (video_id, duration) values (1, 292);
insert into VIDEO (video_id, duration) values (2, 156);
insert into VIDEO (video_id, duration) values (3, 358);
insert into VIDEO (video_id, duration) values (4, 169);
insert into VIDEO (video_id, duration) values (5, 74);
insert into VIDEO (video_id, duration) values (12, 500);



insert into FORMAT (rel_id, format_id) values (1,1);
insert into FORMAT (rel_id, format_id) values (2,2);
insert into FORMAT (rel_id, format_id) values (3,3);
insert into FORMAT (rel_id, format_id) values (4,4);
insert into FORMAT (rel_id, format_id) values (5,5);
insert into FORMAT (rel_id, format_id) values (6,6);
insert into FORMAT (rel_id, format_id) values (7,7);
insert into FORMAT (rel_id, format_id) values (8,8);
insert into FORMAT (rel_id, format_id) values (9,9);
insert into FORMAT (rel_id, format_id) values (10,11);
insert into FORMAT (rel_id, format_id) values (11,12);



insert into DIGITAL (format_id, views) values (1,1000);
insert into DIGITAL (format_id, views) values (2,1001);
insert into DIGITAL (format_id, views) values (3,1002);
insert into DIGITAL (format_id, views) values (4,1003);
insert into DIGITAL (format_id, views) values (5,1004);
insert into DIGITAL (format_id, views) values (9,7);
insert into DIGITAL (format_id, views) values (11, 7000000);



insert into rating (stars, rel_id) values (4,1);
insert into rating (stars, rel_id) values (3,2);
insert into rating (stars, rel_id) values (5,3);
insert into rating (stars, rel_id) values (3,4);
insert into rating (stars, rel_id) values (4,5);
insert into rating (stars, rel_id) values (4,6);
insert into rating (stars, rel_id) values (1,7);
insert into rating (stars, rel_id) values (2,8);
insert into rating (stars, rel_id) values (4,9);

insert into rating (stars, rel_id) values (5,1);
insert into rating (stars, rel_id) values (2,2);
insert into rating (stars, rel_id) values (1,3);
insert into rating (stars, rel_id) values (4,4);
insert into rating (stars, rel_id) values (4,5);
insert into rating (stars, rel_id) values (1,6);
insert into rating (stars, rel_id) values (3,7);
insert into rating (stars, rel_id) values (5,8);
insert into rating (stars, rel_id) values (5,9);

insert into rating (stars, rel_id) values (5,4);
insert into rating (stars, rel_id) values (5,4);
insert into rating (stars, rel_id) values (5,4);
insert into rating (stars, rel_id) values (5,4);

insert into rating (stars, rel_id) values (1,11);
insert into rating (stars, rel_id) values (1,11);
insert into rating (stars, rel_id) values (2,11);
insert into rating (stars, rel_id) values (1,11);

insert into rating (stars, rel_id) values (4,12);
insert into rating (stars, rel_id) values (1,12);
insert into rating (stars, rel_id) values (4,12);
insert into rating (stars, rel_id) values (4,12);

insert into RELEASE (artist_id, rel_id, r_date, release_title, genre_id) values (4, 13, "10/10/2000", "first album", 3);
insert into album (album_id,a_name) values (13,"first album");