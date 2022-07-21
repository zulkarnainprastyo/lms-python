create database lmanage;
 
use lmanage;
SHOW TABLES;

create table books(bname varchar(100) Not null,
  bcode varchar(100) Not null,
  total varchar(100) Not null,
  subject varchar(100) Not null
  );
 
create table issue(name varchar(100) Not null,
 regno varchar(100) Not null,
 bcode varchar(100) Not null,
 idate varchar(100) Not null
 );
 
 create table submit (name varchar(100) Not null,
 regno varchar(100) Not null,
 bcode varchar(100) Not null,
 sdate varchar(100) Not null
 );
 
desc books;
desc issue;
desc submit;

