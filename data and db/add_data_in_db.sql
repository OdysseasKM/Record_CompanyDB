INSERT into GENRE(g_name, g_id) values ('pop',1);
INSERT into GENRE(g_name, g_id) values ('indie, rock',2);
INSERT into GENRE(g_name, g_id) values ('indie',3);
INSERT into GENRE(g_name, g_id) values ('punk',4);
INSERT into GENRE(g_name, g_id) values ('rock',5);
INSERT into GENRE(g_name, g_id) values ('rap',6);
INSERT into GENRE(g_name, g_id) values ('trap',7);
INSERT into GENRE(g_name, g_id) values ('jazz',8);
INSERT into GENRE(g_name, g_id) values ('counrty',9);
INSERT into GENRE(g_name, g_id) values ('hip hop',10);
INSERT into GENRE(g_name, g_id) values ('reggae',11);


INSERT into STUDIO(studio_id,street,number,town,country) values (0,"Korinthou","100","Patras","Greece");
INSERT into STUDIO(studio_id,street,number,town,country) values (1,"Korinthou","74","Patras","Greece");
INSERT into STUDIO(studio_id,street,number,town,country) values (2,"Amalias","24","Athens","Greece");
INSERT into STUDIO(studio_id,street,number,town,country) values (3,"Protagora","13","Volos","Greece");
INSERT into STUDIO(studio_id,street,number,town,country) values (4,"Karaiskaki","42","Athens","Greece");


INSERT into USER (username,password,is_admin) values ("john",1234,true);
INSERT into USER (username,password,is_admin) values ("odysseas",1234,true);
INSERT into USER (username,password,is_admin) values ("test",1234,false);
INSERT into USER (username,password,is_admin) values ("admin",1234,true);

INSERT into INDIVIDUAL (ssn, artist_id, first_name, last_name) values ('221-65-2106', 100, 'Florencia', 'Tuffley');
INSERT into INDIVIDUAL (ssn, artist_id, first_name, last_name) values ('558-21-5235', 101, 'Dorolisa', 'Arpur');
INSERT into INDIVIDUAL (ssn, artist_id, first_name, last_name) values ('705-22-9738', 101, 'Skyler', 'Burmaster');
INSERT into INDIVIDUAL (ssn, artist_id, first_name, last_name) values ('332-16-7794', 101, 'Elayne', 'Newcome');
INSERT into INDIVIDUAL (ssn, artist_id, first_name, last_name) values ('537-83-2675', 102, 'Kippy', 'Champ');
INSERT into INDIVIDUAL (ssn, artist_id, first_name, last_name) values ('116-60-7497', 102, 'Britte', 'Vescovo');
INSERT into INDIVIDUAL (ssn, artist_id, first_name, last_name) values ('749-33-0587', 103, 'Rani', 'Pickring');
INSERT into INDIVIDUAL (ssn, artist_id, first_name, last_name) values ('879-18-8168', 104, 'Bob', 'Brisco');
INSERT into INDIVIDUAL (ssn, artist_id, first_name, last_name) values ('759-57-6257', 105, 'Eve', 'Houten');
INSERT into INDIVIDUAL (ssn, artist_id, first_name, last_name) values ('888-21-4344', 105, 'Stanton', 'Jerromes');
INSERT into INDIVIDUAL (ssn, artist_id, first_name, last_name) values ('874-25-4977', 106, 'Immanuel', 'Ellicock');
INSERT into INDIVIDUAL (ssn, artist_id, first_name, last_name) values ('143-31-6820', 106, 'Thane', 'McKinley');



INSERT into CONTRIBUTOR (last_name, first_name, ssn) values ('Bredgeland', 'Alfie', '532-91-5797');
INSERT into CONTRIBUTOR (last_name, first_name, ssn) values ('Shugg', 'Scotti', '680-59-0854');
INSERT into CONTRIBUTOR (last_name, first_name, ssn) values ('Blazic', 'Wallis', '755-77-0066');
INSERT into CONTRIBUTOR (last_name, first_name, ssn) values ('Loggie', 'Zaccaria', '428-84-0861');
INSERT into CONTRIBUTOR (last_name, first_name, ssn) values ('Carvilla', 'Roselia', '182-17-7378');
INSERT into CONTRIBUTOR (last_name, first_name, ssn) values ('Gosby', 'Josefa', '195-91-7829');
INSERT into CONTRIBUTOR (last_name, first_name, ssn) values ('Bothbie', 'Normy', '449-25-2558');
INSERT into CONTRIBUTOR (last_name, first_name, ssn) values ('Breitler', 'Kasper', '121-78-1884');
INSERT into CONTRIBUTOR (last_name, first_name, ssn) values ('McGilben', 'Arie', '653-81-7206');
INSERT into CONTRIBUTOR (last_name, first_name, ssn) values ('Roderighi', 'Sonja', '168-03-0087');
INSERT into CONTRIBUTOR (last_name, first_name, ssn) values ('Wilton', 'Palmer', '749-60-3632');
INSERT into CONTRIBUTOR (last_name, first_name, ssn) values ('Bithany', 'Tuck', '210-94-7396');
INSERT into CONTRIBUTOR (last_name, first_name, ssn) values ('McGlone', 'Sheppard', '844-87-5599');
INSERT into CONTRIBUTOR (last_name, first_name, ssn) values ('Elderton', 'Conni', '133-61-4534');
INSERT into CONTRIBUTOR (last_name, first_name, ssn) values ('Leech', 'Caro', '743-21-3680');
INSERT into CONTRIBUTOR (last_name, first_name, ssn) values ('Silson', 'Farlie', '347-24-8689');
INSERT into CONTRIBUTOR (last_name, first_name, ssn) values ('Tradewell', 'Idalina', '258-25-8106');
INSERT into CONTRIBUTOR (last_name, first_name, ssn) values ('McAnulty', 'Roseann', '426-38-2985');
INSERT into CONTRIBUTOR (last_name, first_name, ssn) values ('Jancso', 'Fanechka', '712-52-7999');
INSERT into CONTRIBUTOR (last_name, first_name, ssn) values ('Juliano', 'Paige', '825-70-2010');
INSERT into CONTRIBUTOR (last_name, first_name, ssn) values ('Coppens', 'Bob', '420-35-0977');
INSERT into CONTRIBUTOR (last_name, first_name, ssn) values ('Colleton', 'Tabbatha', '397-35-2485');
INSERT into CONTRIBUTOR (last_name, first_name, ssn) values ('Fahrenbacher', 'Hasty', '673-81-5174');
INSERT into CONTRIBUTOR (last_name, first_name, ssn) values ('Gorick', 'Jonie', '617-02-3073');
INSERT into CONTRIBUTOR (last_name, first_name, ssn) values ('Cutbirth', 'Myrta', '480-21-4930');
INSERT into CONTRIBUTOR (last_name, first_name, ssn) values ('Layne', 'Audre', '187-59-9004');
INSERT into CONTRIBUTOR (last_name, first_name, ssn) values ('Rosenboim', 'Paige', '552-63-6946');
INSERT into CONTRIBUTOR (last_name, first_name, ssn) values ('Narup', 'Carolus', '289-49-6102');
INSERT into CONTRIBUTOR (last_name, first_name, ssn) values ('Mendes', 'Wallie', '455-53-2233');
INSERT into CONTRIBUTOR (last_name, first_name, ssn) values ('Clough', 'Bobbi', '781-58-9615');






