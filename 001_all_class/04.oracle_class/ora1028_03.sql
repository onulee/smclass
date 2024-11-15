-- students 학생
-- number(3)
-- varchar2(20) - 문자열
-- no,name,kor,eng,math,total,avg,rank 컬럼을 구성해서 테이블을 구현하시오.

create table students(
 no number(4),
 name varchar2(20),
 kor number(3),
 eng number(3),
 math number(3),
 total number(3),
 avg number(6,2),
 rank number(4) -- 0~9999
);

-- 홍길동,유관순,이순신
-- 1,홍길동,100,100,99,299,99.67,0
-- 2,유관순,80,80,85,245,81.67,0
-- 3,이순신,90,90,91,271,90.33,0


insert into students values(
1,'홍길동',100,100,99,299,99.67,0
);

insert into students values(
2,'유관순',80,80,85,245,81.67,0
);
insert into students values(
3,'이순신',90,90,91,271,90.33,0
);


select * from students;


-- 현재 생성된 테이블 보기
select * from tab;

-- 테이블 타입
desc students;


create table no_tab (
no number,
name varchar2(20),
avg1 number,     -- 소수점 지정없이 선언
avg2 number(5,2) -- 123.23, 소수점지정
);

insert into no_tab values(
1, '홍길동',1000/3,1000/3
);

insert into no_tab values(
2, '유관순',1000/6,500/6
);

insert into no_tab values(
3, '이순신',1000/6,1000/6
);

insert into no_tab values(
4, '강감찬',100/6,100/6
);

select * from no_tab;

create table date_tab (
no number(4),
s_date date,
s_date2 date
);

-- sysdate 현재시간
insert into date_tab values(
1,'2024-09-28',sysdate
);

select * from date_tab;

select to_char(s_date,'YYYY-MM-DD'),to_char(s_date2,'yyyy-mm-dd hh24:mi:ss') from date_tab;

select to_char(s_date,'yyyy-mm-dd hh:mi:ss'),to_char(s_date2,'yyyy-mm-dd hh24:mi:ss') from date_tab;

-- 검색
-- select 컬럼명 from 테이블명
-- select * (모든컬럼의미) from 테이블명
select * from employees;
select employee_id,emp_name,salary from employees;
select EMP_NAME from employees;

SELECT EMP_NAME FROM EMPLOYEES;
select emp_name from employees;

select emp_name from employees where emp_name = 'pat Fay';

select * from employees;

-- 사원번호,사원명 전화번호,입사일(hire_date) 컬럼만 출력하시오.
select employee_id,emp_name,phone_number,hire_date from employees;

-- 사원번호, 사원명, 직급번호(job_id) SH CLERK 사원만 출력하시오.
select employee_id,emp_name,job_id from employees;
select employee_id,emp_name,job_id from employees where job_id = 'SH_CLERK';

-- 테이블 삭제
-- drop table member;

create table member (
	id VARCHAR2(50),
	pw varchar2(4),
	name VARCHAR2(50),
	email VARCHAR2(50),
	phone VARCHAR2(50),
	gender VARCHAR2(50),
	hobby varchar2(50),
	mdate DATE
);
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('aaa', '1111', '홍길동', 'rsherville0@tinyurl.com', '324-226-8544', 'Male', 'golf', '2024-03-06');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('bbb', '1111', '유관순', 'mrubinlicht1@fotki.com', '475-964-8193', 'Female', 'book', '2024-08-18');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('ccc', '1111', '이순신', 'bchstney2@walmart.com', '541-891-0085', 'Female', 'run', '2024-08-16');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('ddd', '1111', '강감찬', 'cstubbes3@chron.com', '900-194-4605', 'Female', 'game', '2024-02-10');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('eee', '1111', '김구', 'tnacey4@list-manage.com', '727-883-1542', 'Female', 'golf', '2024-09-10');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Trineman', '6216', 'Riobard', 'rtrineman5@prweb.com', '140-720-7698', 'Male', 'book', '2024-09-03');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Towell', '5201', 'Bryan', 'btowell6@stumbleupon.com', '365-214-7874', 'Male', 'run', '2024-03-16');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Neagle', '4903', 'Horacio', 'hneagle7@nifty.com', '114-384-4352', 'Male', 'run', '2024-02-01');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Gresham', '4089', 'Valentine', 'vgresham8@quantcast.com', '547-694-3516', 'Female', 'swim', '2024-10-11');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('O''Dare', '6041', 'Doroteya', 'dodare9@dyndns.org', '102-500-7735', 'Female', 'game', '2024-07-29');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Doumic', '1343', 'Stepha', 'sdoumica@com.com', '745-998-5005', 'Female', 'game', '2024-08-08');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Allmann', '9173', 'Husein', 'hallmannb@imageshack.us', '122-775-3647', 'Male', 'book', '2024-01-01');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Tommis', '6716', 'Roderic', 'rtommisc@sourceforge.net', '673-244-8303', 'Male', 'book', '2024-07-09');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Bleaden', '4168', 'Drud', 'dbleadend@123-reg.co.uk', '838-544-2408', 'Male', 'golf', '2024-06-18');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('D''Aguanno', '7476', 'Wini', 'wdaguannoe@cyberchimps.com', '237-714-1340', 'Female', 'run', '2024-06-27');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Gegay', '8185', 'Bernette', 'bgegayf@yahoo.com', '982-358-5670', 'Female', 'golf', '2024-07-05');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Flea', '6937', 'Fidelity', 'ffleag@reverbnation.com', '602-708-0462', 'Female', 'run', '2024-01-18');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Shory', '1240', 'Robb', 'rshoryh@intel.com', '621-231-3542', 'Male', 'run', '2024-09-13');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Harm', '1438', 'Flinn', 'fharmi@yelp.com', '328-792-9216', 'Male', 'golf', '2023-12-05');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Poschel', '9693', 'Sterling', 'sposchelj@usnews.com', '499-462-1400', 'Male', 'swim', '2024-05-27');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Medford', '5717', 'Jacquenette', 'jmedfordk@epa.gov', '634-270-7550', 'Female', 'book', '2024-02-18');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Gianelli', '5559', 'Katherina', 'kgianellil@wikipedia.org', '967-878-2128', 'Female', 'game', '2024-05-18');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Kolodziejski', '5522', 'Danella', 'dkolodziejskim@jugem.jp', '110-354-1019', 'Female', 'golf', '2024-03-25');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Mildmott', '9678', 'Jule', 'jmildmottn@wix.com', '286-208-5611', 'Male', 'run', '2024-07-23');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Pietrowski', '6843', 'Ediva', 'epietrowskio@photobucket.com', '571-362-5389', 'Female', 'golf', '2023-12-30');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Chasemoore', '9290', 'Dunc', 'dchasemoorep@geocities.jp', '390-444-9215', 'Male', 'golf', '2024-03-27');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Overnell', '6410', 'Barth', 'bovernellq@cdbaby.com', '825-465-2790', 'Male', 'run', '2024-06-12');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Benford', '8906', 'Margette', 'mbenfordr@twitter.com', '210-839-4892', 'Female', 'swim', '2024-06-20');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Portman', '6013', 'Orson', 'oportmans@reverbnation.com', '258-285-2186', 'Male', 'golf', '2024-06-09');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Elflain', '7065', 'Trish', 'telflaint@intel.com', '319-787-3297', 'Female', 'golf', '2024-04-30');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Ockland', '7153', 'Deirdre', 'docklandu@sfgate.com', '895-501-5958', 'Female', 'run', '2023-12-03');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Le Floch', '5518', 'Linea', 'lleflochv@hp.com', '734-888-6261', 'Female', 'swim', '2024-01-24');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('McGaugan', '5439', 'Conny', 'cmcgauganw@imageshack.us', '376-451-4038', 'Male', 'game', '2023-11-08');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Lilburn', '6148', 'Shepherd', 'slilburnx@sina.com.cn', '250-173-1654', 'Male', 'swim', '2024-07-03');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Frew', '7401', 'Meaghan', 'mfrewy@unc.edu', '276-431-6409', 'Female', 'swim', '2023-12-04');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Myner', '1917', 'Lorrie', 'lmynerz@wikimedia.org', '550-264-0011', 'Male', 'book', '2024-10-06');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Knightsbridge', '2295', 'Elias', 'eknightsbridge10@dedecms.com', '906-789-7346', 'Male', 'swim', '2023-12-30');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Merwood', '6745', 'Georgy', 'gmerwood11@comcast.net', '904-984-7938', 'Male', 'golf', '2024-01-14');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Dewsbury', '1477', 'Bond', 'bdewsbury12@amazon.co.jp', '106-232-5734', 'Male', 'swim', '2024-02-02');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Kliche', '5468', 'Nevins', 'nkliche13@admin.ch', '608-113-7174', 'Male', 'game', '2024-06-22');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Fick', '7675', 'Panchito', 'pfick14@senate.gov', '430-438-4575', 'Male', 'book', '2024-03-12');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Danielczyk', '5661', 'Reinaldos', 'rdanielczyk15@irs.gov', '359-176-0405', 'Male', 'book', '2024-05-27');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Blazey', '8853', 'Lou', 'lblazey16@about.com', '729-460-3951', 'Male', 'run', '2024-04-12');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Godly', '6603', 'Pail', 'pgodly17@plala.or.jp', '190-426-8746', 'Male', 'run', '2024-06-02');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Attwoull', '3472', 'Cliff', 'cattwoull18@slideshare.net', '570-758-4710', 'Male', 'golf', '2024-08-10');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Chason', '5763', 'Terrie', 'tchason19@symantec.com', '650-189-0579', 'Female', 'run', '2024-03-11');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Noni', '2224', 'Jannel', 'jnoni1a@bloglovin.com', '871-506-4522', 'Female', 'book', '2024-01-04');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Graham', '3477', 'Mendy', 'mgraham1b@trellian.com', '887-280-4803', 'Male', 'swim', '2024-09-01');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Griffey', '8521', 'Raff', 'rgriffey1c@51.la', '947-561-4983', 'Male', 'swim', '2024-04-12');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Wretham', '3484', 'Laure', 'lwretham1d@ted.com', '183-800-2897', 'Female', 'book', '2023-11-07');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Sewart', '5890', 'Lodovico', 'lsewart1e@shareasale.com', '962-952-9409', 'Male', 'swim', '2024-05-25');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Leber', '3162', 'Cory', 'cleber1f@foxnews.com', '773-506-6136', 'Female', 'run', '2024-05-03');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Germain', '2786', 'Teodoor', 'tgermain1g@usda.gov', '287-887-6296', 'Male', 'book', '2024-09-25');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('O''Dooghaine', '4249', 'Jeni', 'jodooghaine1h@washingtonpost.com', '656-654-8738', 'Female', 'book', '2024-02-18');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Ralestone', '2620', 'Lenard', 'lralestone1i@w3.org', '692-797-1702', 'Male', 'book', '2024-09-07');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Yong', '8340', 'Kasey', 'kyong1j@seattletimes.com', '820-634-7148', 'Female', 'run', '2023-12-04');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Yukhov', '6010', 'Gallard', 'gyukhov1k@weather.com', '602-990-8790', 'Male', 'run', '2023-12-22');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Digman', '1555', 'Britt', 'bdigman1l@google.com', '997-747-6638', 'Female', 'game', '2023-11-04');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Rocks', '1647', 'Dane', 'drocks1m@latimes.com', '455-553-6937', 'Male', 'book', '2023-12-07');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Lewisham', '8757', 'Danni', 'dlewisham1n@addtoany.com', '597-704-9376', 'Female', 'swim', '2024-02-09');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('O''Spillane', '4868', 'Hamlen', 'hospillane1o@indiegogo.com', '584-856-0076', 'Male', 'golf', '2024-02-19');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Keoghane', '8511', 'Garrott', 'gkeoghane1p@accuweather.com', '655-285-1122', 'Male', 'game', '2024-01-23');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Gransden', '3139', 'Maire', 'mgransden1q@bloglines.com', '517-233-8716', 'Female', 'book', '2024-02-24');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Kobiera', '5689', 'Jaime', 'jkobiera1r@flickr.com', '325-635-7089', 'Female', 'run', '2023-11-16');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Craske', '6088', 'Isa', 'icraske1s@delicious.com', '903-771-5929', 'Male', 'golf', '2024-06-26');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Island', '9324', 'Terrance', 'tisland1t@cmu.edu', '569-238-3939', 'Male', 'golf', '2024-03-16');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Hazeldine', '9138', 'Glenn', 'ghazeldine1u@foxnews.com', '118-455-4847', 'Male', 'game', '2024-08-10');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Gutch', '8827', 'Davin', 'dgutch1v@jiathis.com', '602-127-7922', 'Male', 'book', '2024-07-06');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Pavlenkov', '8269', 'Elane', 'epavlenkov1w@cyberchimps.com', '172-572-0209', 'Female', 'game', '2023-12-27');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Kasman', '3887', 'Davita', 'dkasman1x@de.vu', '140-813-6914', 'Female', 'book', '2024-09-15');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Andraud', '6948', 'Gunter', 'gandraud1y@rambler.ru', '999-479-2224', 'Male', 'swim', '2024-03-10');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Mandrey', '9531', 'My', 'mmandrey1z@whitehouse.gov', '809-354-8112', 'Male', 'golf', '2024-04-17');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Teers', '1997', 'Lynda', 'lteers20@bigcartel.com', '831-197-8592', 'Female', 'golf', '2024-07-28');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('MacBey', '8775', 'Farand', 'fmacbey21@seesaa.net', '319-735-6030', 'Female', 'swim', '2024-06-05');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Bontoft', '2628', 'Blanca', 'bbontoft22@webnode.com', '818-469-6633', 'Female', 'run', '2024-09-25');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Gercken', '3185', 'Heinrik', 'hgercken23@webmd.com', '604-301-2929', 'Male', 'game', '2024-03-28');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Huzzay', '5857', 'Alf', 'ahuzzay24@sogou.com', '570-223-4310', 'Male', 'book', '2024-08-16');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Tredger', '7675', 'Sherwood', 'stredger25@bbc.co.uk', '527-871-8185', 'Male', 'run', '2024-06-01');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Canadine', '8566', 'Nicolis', 'ncanadine26@devhub.com', '800-674-8410', 'Male', 'golf', '2024-08-03');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Paireman', '7080', 'Nichol', 'npaireman27@msn.com', '668-411-8679', 'Female', 'run', '2024-01-01');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Powis', '6242', 'Mehetabel', 'mpowis28@surveymonkey.com', '271-883-5391', 'Female', 'book', '2024-09-18');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Walsh', '7311', 'Luther', 'lwalsh29@gmpg.org', '523-360-3018', 'Male', 'golf', '2024-09-18');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Pont', '4975', 'Edd', 'epont2a@nbcnews.com', '551-629-4794', 'Male', 'golf', '2024-02-22');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Osborne', '7007', 'Gauthier', 'gosborne2b@naver.com', '711-842-1931', 'Male', 'run', '2024-05-31');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Tinker', '8402', 'Andree', 'atinker2c@wp.com', '731-985-8198', 'Female', 'swim', '2023-12-23');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Persence', '7577', 'Obediah', 'opersence2d@elegantthemes.com', '549-594-4369', 'Male', 'run', '2024-05-28');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Boatwright', '1204', 'Ernie', 'eboatwright2e@printfriendly.com', '833-853-7804', 'Male', 'swim', '2024-01-18');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Kirkhouse', '6330', 'Pernell', 'pkirkhouse2f@soup.io', '412-173-6891', 'Male', 'book', '2024-06-12');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Ghidetti', '9376', 'Den', 'dghidetti2g@seattletimes.com', '165-768-1973', 'Male', 'run', '2024-10-21');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Keppel', '1397', 'Yolanthe', 'ykeppel2h@harvard.edu', '928-660-5279', 'Female', 'run', '2024-09-09');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Matteini', '7664', 'Zola', 'zmatteini2i@jalbum.net', '672-317-8567', 'Female', 'swim', '2024-05-28');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Malmar', '9156', 'Andriana', 'amalmar2j@ed.gov', '588-732-4548', 'Female', 'run', '2024-01-25');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Waplington', '7863', 'Tobiah', 'twaplington2k@dell.com', '996-187-6594', 'Male', 'game', '2024-07-11');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Cosyns', '2387', 'Lauri', 'lcosyns2l@edublogs.org', '943-340-9913', 'Female', 'game', '2024-04-05');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Atto', '5832', 'Had', 'hatto2m@mozilla.com', '624-750-8503', 'Male', 'game', '2024-06-07');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Bushell', '8202', 'Franz', 'fbushell2n@indiegogo.com', '274-938-6045', 'Male', 'game', '2024-03-06');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Glassford', '3189', 'Virgil', 'vglassford2o@usatoday.com', '361-318-5270', 'Male', 'run', '2024-05-23');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Aron', '3277', 'Freeland', 'faron2p@timesonline.co.uk', '724-482-5099', 'Male', 'game', '2024-08-25');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Tavner', '8684', 'Brig', 'btavner2q@webeden.co.uk', '366-125-0586', 'Male', 'run', '2024-05-14');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Shiliton', '5557', 'Sandi', 'sshiliton2r@abc.net.au', '407-488-9852', 'Female', 'book', '2024-01-11');

commit;

select * from member;


-- 테이블 생성(create), 삭제(drop)
-- 데이터추가(insert), 검색(select) ,삭제(delete), 수정(update)

-- delete member;
rollback;
select * from member;

-- 삭제, where조건절 컬럼에 해당되는 값
delete member where id='Trineman';
commit;
delete member where gender ='Male';
rollback;

delete member where gender = 'Male' and hobby='golf';
rollback;

delete member where gender = 'Male' or hobby='golf';
rollback;

delete students where name='홍길동';
rollback;
delete students where name='유관순';
rollback;

-- 수정
select * from member;
update member set name='김유신' where id='Towell';
select * from member;
commit;

update member set id = 'fff' where id ='Towell';
select * from member;
commit;

update member set id = 'ggg', name='홍길자' where id='Neagle';
select * from member;
commit;

-- 취미:swim -> bike
update member set hobby='bike' where hobby='swim';
select * from member;
rollback;

-- 숫자인 경우만, 연산자가 가능.
-- 타입 : 숫자인경우 +,-,*,/
select * from students;
select name,(kor+eng),kor+math from students;
select name,(total-kor)/2 from students;

select * from employees;
-- 사원월급이 달러표기 -> 원화 환산 하시오.
select salary from employees;
select salary,to_char(salary*1384.66,'999,999,999') from employees;


-- member회원 수
select count(*) from member;

-- member회원 출력
select * from member;
