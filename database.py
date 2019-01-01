create database logindb;
create table itemss(
	name varchar(80) not null,
	imageName longblob not null,
	videoName longblob not null,
	audioName longblob not null);
select name,substring(imageName,1,20),substring(videoName,1,20),substring(audioName,1,20) from itemss;