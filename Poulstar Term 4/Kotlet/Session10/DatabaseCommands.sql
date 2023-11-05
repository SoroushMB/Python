create database kotletstore;
use kotletstore;
create table laptop(
	IDNumber int unsigned auto_increment not null unique,
    ModelName varchar(250) not null unique,
    CPUModel varchar(60) not null,
    GPUModel varchar(60) not null,
    RAM varchar(10) not null,
    Display varchar(100) not null,
    Battery varchar(50) not null,
    InternalStorage varchar(40) not null
);
insert into laptop
values (1,"MacBook Pro 14 2023","Apple M3,M3 Pro,M3 Max",
		"10-Cores,14-Cores,18-Cores,30-Cores","8GB-128GB",
        "14,QHD+,Liquid Retina XDR","22-Hours","512GB-8TB");
select * from laptop;
