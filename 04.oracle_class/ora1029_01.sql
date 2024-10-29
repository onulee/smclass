-- drop table member;
-- drop table date_tab;
-- drop table no_tab;
-- drop table students;

-- create 테이블 생성, alter 테이블 수정, drop 테이블 삭제 
create table member(
 no number(4),
 id varchar2(20),
 pw varchar2(20),
 name varchar2(20),
 phone varchar2(20),
 mdate date
);

-- insert 데이터 입력 , select 데이터 검색, update 데이터 수정, delete 데이터 삭제
insert into member values(
1,'aaa','1111','홍길동','010-1111-1111','2024-10-29'
);

insert into member values(
2,'bbb','1111','유관순','010-2222-2222','2024-09-20'
);


-- select 데이터 검색
select * from member;

commit;
rollback;

-- delete 삭제
-- delete member where no=2;
-- delete member;

-- update 수정
update member set name='홍길자' where no=1;
update member set name='김구';

select * from member;

-- create 테이블 생성
create table students (
stuno number(4),
name varchar2(20),
kor number(3),
eng number(3),
total number(3),
sdate date
);
-- sysdate :현재날짜,시간저장
insert into students values(
1,'홍길동',100,100,100+100,sysdate
);

commit;

-- * 모든 컬럼 검색
select * from students;

-- 특정컬럼을 입력하면 컬럼만 검색
select name,sdate from students;

-- 특정컬럼만 입력하면 컬럼입력
insert into students (stuno,name) values(
2,'유관순'
);

select * from students;

-- 
select * from employees;
select count(*) from employees;

----------
-- 테이블을 생성하면서 테이블 내용을 모두 복사
create table emp2 as select * from employees;
select * from emp2;
select count(*) from emp2; -- 데이터 개수

-- 테이블을 생성하면서 테이블 구조만 복사
create table emp3 as select * from employees where 1=2;
select * from emp3;

-- 테이블이 존재 할 경우 데이터만 복사
create table member2 as select * from member where 1=2;
insert into member2 select * from member;


-- 테이블 컬럼 
-- 컬럼데이터 타입, 길이 변경
-- alter변경 member테이블 no컬럼의 타입길이를 변경
alter table member modify no number(10);
-- alter변경, 컬럼의 이름을 변경
alter table member rename column no to memberNo;

-- 테이블 구조
desc employees;

-- employees 테이블에서 사원번호(employee_id),사원이름(emp_name), 입사일hire_date
select employee_id,emp_name,hire_date 
from employees;

select * from employees;

-- 연산자 : 산술연산자, +,-,*,/

select kor,eng,(kor+eng) from students;
select kor,eng,(kor+eng),abs(kor-eng) from students;

select * from employees;

-- 문자 더하기안됨.
select employee_id+emp_name from employees;

-- concat 명령어, ||
select concat(employee_id,emp_name) from employees;
select employee_id||emp_name from employees;

-- 달러환산 1384
select salary from employees;
select salary*1384 from employees;
-- 문자로 변환, 천단위 표시
select to_char(salary*1384,'999,999,999') from employees;
select emp_name,salary,salary*1384 from employees;

create table stu(
no number(4),
name varchar2(20),
kor number(3)
);

-- null값 검색 is null
select * from stu where name is null;

-- null이 아닌것 출력 : is not null
select commission_pct from employees where commission_pct is not null;

select salary from employees;
-- 년봉계산 * 12
select salary, salary*12 from employees;
select salary, salary*12, salary*12*1384 from employees;

-- 커미션이 없는 사원은 null값이 있는데, null +,-,*,/ null값으로 변경
select salary,salary*12,salary*12+(salary*12)*commission_pct*0.01 from employees;

-- 컬럼명 별칭 사용 as, "" 특수문자, 사이공간까지 컬럼명으로 사용가능
select salary,salary*12 as "년 봉",salary*12+(salary*12)*nvl(commission_pct,0)*0.01 as "r e al_yearSalary" from employees;

-- nvl() 함수, nvl(kor,0) : kor컬럼에 null값이 있으면 0으로 표시
select * from stu;
select no,name,kor,kor+100 from stu;
select no,name,kor,nvl(kor,0)+100 from stu;

-- 번호,이름,국어,영어,수학,합계,평균,등수,입력일 
-- 컬럼명 별칭을 사용해서 출력하시오.
select no as 번호,name as 이름, kor 국어, eng "영   어",math 수학,total 합계,avg 평균,sdate 입력일 
from students;
select * from students;

-- 사원번호,이름,이메일을 합쳐서 출력하시오.
select employee_id||emp_name||email from employees;
select concat(concat(employee_id,emp_name),email) from employees;
select emp_name||' is a ' ||job_id from employees;

-- 중복제거 : distinct
select department_id from employees;
select distinct department_id from employees ;
-- 정렬 : order by - asc 순차정렬: 생략가능, desc - 역순정렬
select distinct department_id from employees order by department_id desc;


-- job_id 중복제거 출력하시오.
select distinct job_id from employees;
select job_id from employees;

-- 문자열자르기 substr(0,2) 0,1  ,2앞에 까지 출력
select substr(job_id,0,2) from employees;

-- 4번째 컬럼데이터를 가져와서 중복을 제거 함.
select distinct substr(job_id,4) from employees;


-- where절 : 조건비교연산자 >,<,>=,<=,=,!=
select * from employees where manager_id != 124;
select * from employees where job_id = 'SH_CLERK';
select * from employees where employee_id >100;

-- students 합계 250 이상 출력하시오.
select * from students where total >= 250;

-- 합계250, kor 90점이상 출력하시오.
select * from students where total >=250 and kor >= 90;

-- 영어점수 70 이상, 90 이하 출력하시오.
select * from students where eng>=70 and eng<=90;
-- select * from students where 70<= eng <=90;

-- 월급이 5000이상 8000이하 출력하시오.
select * from employees where salary>=5000 and salary<=8000;

-- 7000이 아닌 것을 출력하시오. !=, <>, ^=
select * from employees where salary != 7000;

-- 부서(department_id) = 50  
-- count 개수확인
select * from employees where department_id = 50;
select count(*) from employees where department_id = 50;  --45

-- 50번이 아닌것 출력하시오.
select * from employees where department_id != 50;
select count(*) from employees where department_id != 50;  -- 61 106개

-- null값은 count() 포함되지 않음.
select count(*) from employees;
select count(*) from employees where department_id is null;  -- 1개
select count(employee_id) from employees;    -- 107개
select count(department_id) from employees;  -- 106개 , null값이 1개가 있기에 106개가 나옴.

-- 급여 4000이하 사원번호,사원명,급여 컬럼만 출력하시오.
select * from employees where salary <= 4000;
select employee_id as 사원번호,emp_name 사원명,salary 급여 from employees where salary <= 4000;

-- 숫자 비교연산자 가능, 날짜 비교연산자가 가능
select emp_name,hire_date from employees;

select emp_name,hire_date from employees where hire_date >= '2002/01/01';

-- 1999/12/31 이전에 입사한 사람을 출력하시오.
select emp_name,hire_date from employees where hire_date <= '1999/12/31';

-- 2001/01/01 부터 2004/12/31 까지 출력하시오.
select emp_name,hire_date from employees
where hire_date>='20010101' and hire_date<='20041231';


-- 논리연산자
-- 국어점수가 90점이상 또는 영어점수가 90점이상을 출력하시오. students테이블
select count(*) from students where kor>=90 or eng>=90;  -- 41
select count(*) from students where kor>=90 and eng>=90; -- 3
select count(*) from students where not kor>=90;


-- 부서번호(department_id) - 80 이면서  job_id - MAN
select * from employees;
select substr(job_id,4) from employees;
select * from employees where department_id = 80 and substr(job_id,4) = 'MAN';
select * from employees where department_id = 80 and job_id = 'SA_MAN';


-- 커미션이 0.2,0.3,0.5 인 경우만 출력하시오.
-- or연산자 사용
select commission_pct from employees where commission_pct is not null;
select commission_pct from employees 
where
commission_pct=0.2 or commission_pct=0.3 or commission_pct=0.5;
-- in 연산자
select commission_pct from employees
where
commission_pct in (0.2,0.3,0.5);

-- 사원번호 (employee_id ) 110,120,130 출력하시오.
select * from employees;
select * from employees where
employee_id = 110 or employee_id = 120 or employee_id = 130;

select * from employees where
employee_id in (110,120,130);

-- 150-170 사원번호를 출력하시오.
select * from employees where employee_id >= 150 and employee_id <= 170;


-- between - and : <= 포함이 되어 있는 경우만 해당
select * from employees
where employee_id between 150 and 170;

-- 날짜 in
select hire_date from employees;
select hire_date from employees
where hire_date in ('2004/02/17','2002/06/07');

-- 날짜 between
select hire_date from employees
where hire_date between '2002/06/17' and '2004/12/31';

-- job MAN 출력하시오.
select * from employees
where substr(job_id,4) = 'MAN';

-- LIKE연산자 : 포함되어 있는 글자 검색
select * from employees
where job_id = 'MAN';

-- MAN으로 끝나는 단어를 검색
select * from employees
where job_id like '%MAN';
-- ST시작되는 단어를 검색
select * from employees
where job_id like 'ST%';

-- EMP_NAME a가 들어가 있는 이름 출력하시오.
select * from employees
where emp_name not like '%a%';

-- 2번째 자리에 t 가 들어가 있는 이름 출력하시오.
select * from employees
where emp_name like '_t%';

-- 4번째 v가 들어가 있는 이름 출력하시오.
select * from employees
where emp_name like '___v%';

-- 뒤에서 2번째 자리에 l에 가 있는 이름을 출력하시오.
select * from employees
where emp_name like '%l_';

-- 첫번째 D가 들어가 있는 이름을 출력하시오.
select * from employees
where emp_name like 'D%';






























