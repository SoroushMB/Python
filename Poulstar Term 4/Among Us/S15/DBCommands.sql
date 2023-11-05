-- drop database cars_companies;
create database cars_companies;
use cars_companies;
create table cars(
    id int unsigned unique not null auto_increment,
    primary key (id),
    car_model varchar(80) not null,
    ...
);
drop table cars;