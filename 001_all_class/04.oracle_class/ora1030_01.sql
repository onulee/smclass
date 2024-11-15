select sysdate from dual;

select sysdate-30,sysdate,sysdate+30 from dual;

-- employees테이블 hire_date 컬럼
select hire_date-1,hire_date,hire_date+1 from employees;

-- 날짜 범위 검색가능, 정렬 order by , asc:순차정렬, desc:역순정렬
select emp_name,hire_date from employees 
where hire_date>='02/01/01' and hire_date<='04/12/31'
order by hire_date desc
;

select emp_name,hire_date from employees
where hire_date between '02/01/01' and '04/12/31'
order by hire_date;

-- like
select emp_name from employees
where emp_name like '___a%';

select emp_name from employees
where emp_name like '%a_';


-- 정렬 desc : null값이 제일 위에 검색, asc:제일 아래에 검색
select department_id from employees
order by department_id desc;

-- 월급(salary) 역순정렬
select emp_name,salary from employees
order by salary desc;

-- students테이블에서 total 역순정렬
select no,name,total from students
order by total desc;

-- hire_date 기준, 순차정렬
select * from employees
order by hire_date asc;

select name,kor,eng,math from students
order by kor desc, eng desc;

select name,kor,eng,math from students
order by kor desc;

-- 한국어 순차정렬:ㄱ,ㄴ,ㄷ... 역순정렬 : ㅎ,ㅌ,ㅍ,ㅋ,...
select name from students
order by name;


-- 입사일이 빠른 순으로 정렬하는데, 이름은 역순으로 정렬하시오.
select emp_name,hire_date from employees
order by hire_date asc,emp_name desc;


-- abs 절대값
select -10 val,abs(-10) as abs from dual;

select kor,kor-eng,abs(kor-eng) abs from students
order by abs desc
;

-- floor 소수점 이하 버림
select 3.141592 ,floor(3.141592) from dual;
-- trunc : 버림, 자리수 지정
select 34.5678,trunc(34.5678,2) from dual;
select 34.5678,trunc(34.5678,-1) from dual;

-- ceil 소수점 이하 올림
select 3.14592, ceil(3.141592) from dual;

-- round 반올림, 자리수 범위지정
-- 소수점 첫째자리
select 34.5678, round(34.5678) from dual;
-- 소수점 둘째자리까지 출력, 셋째자리에서 반올림 됨.
select 34.5678, round(34.5678,2) from dual;
-- 양수 첫째자리에서 반올림, 소수점자리수에서 앞쪽으로 한칸위치 반올림.
select 34.5678, round(35.5678,-1) from dual;

-- mod : 나머지
select 27/2,mod(27,2) from dual;
select 30/3, mod(31,7) from dual;

-- 사원번호가 홀수 인 사원을 출력하시오.
-- 나머지가 1인 mod(employee_id,2) = 1

select employee_id,emp_name from employees
where mod(employee_id,2) = 1
order by employee_id;

select commission_pct from employees
where commission_pct is not null;

-- 1381.86
-- 최종연봉 : 월급*12+(월급*12)*커미션 , 소수점 2자리에서 반올림. 첫째자리로 만들시오.
select salary,round(salary*12+((salary*12)*nvl(commission_pct,0))*1381.86795,1) ysalary from employees;

select * from students;



-- 시퀀스 : 자동으로 번호부여
create sequence stu_seq
start with 1
increment by 1
minvalue 1
maxvalue 9999
nocycle
nocache;

-- 시퀀스에서 번호생성
select stu_seq.nextval from dual;

select stu_seq.currval from dual;

-- 게시판 테이블 생성
create table board(
bno number(4),
btitle varchar2(100),
bcontent varchar2(4000),
id varchar2(30),
bhit number(10),
bdate date
);

insert into board values(
1,'제목입니다.','내용입니다.','aaa',1,sysdate
);

insert into board values(
2,'제목입니다.2','내용입니다.2','aaa',1,sysdate
);

insert into board values(
stu_seq.nextval,'제목입니다.2','내용입니다.2','aaa',1,sysdate
);

select * from board;
commit;

















