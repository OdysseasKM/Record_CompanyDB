insert into ARTIST (id,nickname,country) values (1, "john", "greece");
insert into ARTIST (id,nickname,country) values (2, "ody", "greece");
insert into ARTIST (id,nickname,country) values (3, "john the great", "greece");
insert into ARTIST (id,nickname,country) values (4, "ody", "greece");
insert into ARTIST (id,nickname,country) values (5, "demitria", "albania");

insert into RELEASE (artist_id, release_id, r_date, release_title) values (1, 1, "10/10/2000", "new release");
insert into RELEASE (artist_id, release_id, r_date, release_title) values (1, 2, "10/10/2000", "new release1");
insert into RELEASE (artist_id, release_id, r_date, release_title) values (1, 3, "10/10/2000", "new release2");
insert into RELEASE (artist_id, release_id, r_date, release_title) values (2, 4, "10/10/2000", "new release3");
insert into RELEASE (artist_id, release_id, r_date, release_title) values (2, 5, "10/10/2000", "new release4");
insert into RELEASE (artist_id, release_id, r_date, release_title) values (2, 6, "10/10/2000", "new release5");
insert into RELEASE (artist_id, release_id, r_date, release_title) values (3, 7, "10/10/2000", "new release6");
insert into RELEASE (artist_id, release_id, r_date, release_title) values (3, 8, "10/10/2000", "new release7");
insert into RELEASE (artist_id, release_id, r_date, release_title) values (3, 9, "10/10/2000", "new release8");
insert into RELEASE (artist_id, release_id, r_date, release_title) values (3, 10, "10/10/2000", "new release8");
insert into RELEASE (artist_id, release_id, r_date, release_title) values (5, 11, "10/10/2000", "kapsoura 8 mwromou");
insert into RELEASE (artist_id, release_id, r_date, release_title) values (5, 12, "10/10/2000", "stepbrother i am stuck / hot mommy milker mom");

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


INSERT into GENRE(name, rel_id) values ('pop',1);
INSERT into GENRE(name, rel_id) values ('pop',2);
INSERT into GENRE(name, rel_id) values ('indie',3);
INSERT into GENRE(name, rel_id) values ('pop',4);
INSERT into GENRE(name, rel_id) values ('pop',5);
INSERT into GENRE(name, rel_id) values ('indie',6);
INSERT into GENRE(name, rel_id) values ('pop',7);
INSERT into GENRE(name, rel_id) values ('pop',8);
INSERT into GENRE(name, rel_id) values ('indie',9);
INSERT into GENRE(name, rel_id) values ('laikh-indie',11);
INSERT into GENRE(name, rel_id) values ('punk',12);
INSERT into GENRE(name, rel_id) values ('trap',12);

insert into FORMAT (format_id) values (1);
insert into FORMAT (format_id) values (2);
insert into FORMAT (format_id) values (3);
insert into FORMAT (format_id) values (4);
insert into FORMAT (format_id) values (5);
insert into FORMAT (format_id) values (6);
insert into FORMAT (format_id) values (7);
insert into FORMAT (format_id) values (8);
insert into FORMAT (format_id) values (9);
insert into FORMAT (format_id) values (11);
insert into FORMAT (format_id) values (12);



insert into ONLINE (id, views) values (1,1000);
insert into ONLINE (id, views) values (2,1001);
insert into ONLINE (id, views) values (3,1002);
insert into ONLINE (id, views) values (4,1003);
insert into ONLINE (id, views) values (5,1004);
insert into ONLINE (id, views) values (11, 7000000);
insert into ONLINE (id, views) values (12,7);


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