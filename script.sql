create database ponto;
use ponto;
create table registro_ponto(
Email varchar(255) primary key not null,
Nome varchar(255) not null,
#YYYY-MM-DD hh:mm:ss 
Data_hora datetime);