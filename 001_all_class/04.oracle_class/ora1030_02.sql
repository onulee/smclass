select * from board;

create sequence board_seq
start with 14      -- 시작번호
increment by 1  -- 증감숫자
minvalue 1         -- 최소값
maxvalue 9999   -- 최대값
nocycle               -- 1-9999 이상이되면 , 다시 1
nocache              -- 메모리에 시퀀스값 미리할당
;

desc board;

insert into board values(
board_seq.nextval,'제목14','내용14','aaa',1,sysdate
);

select * from board;

update board set btitle='제목을 다시 변경' where bno=14;

commit;


drop table board;

create table board(
bno number(4),
btitle varchar2(100),
bcontent clob, -- 대용량 글자타입
id varchar2(20),
bgroup number(4), -- 답변달기 그룹핑
bstep number(4),    -- 답변달기 경우 순서정의
bindent number(4),  -- 답변달기 드려쓰기
bhit number(10),      -- 조회수
bdate date                -- 등록일
);

select board_seq.currval from dual;

insert into board values(
board_seq.nextval, '제목1','내용1','aaa',board_seq.currval,0,0,1,sysdate
);

select * from board;

-- 시퀀스 생성
-- students_seq.nextval
-- students 테이블 100 -> 101
-- 101,'홍길순',99,99,90,total,avg,rank,날짜
-- 1명을 입력하시오.

insert into students values(
students_seq.nextval,'홍길순',99,99,90,99+99+90,(99+99+90)/3,0,sysdate
);

select * from students;

-- delete students where name='홍길순';

commit;

select no,name,kor,eng,math,total,round(avg,2),rank,sdate
from students;

select * from students;
select *,round(avg,2) from students;

select s.*,round(avg,2) from students s;


select dept_seq.nextval from dual;

-- s_seq
-- 시작 1,증분1 최대값 99999

create sequence s_seq
start with 1
increment by 1
minvalue 1
maxvalue 99999
nocache
nocycle
;

--  시퀀스 생성, nextval : 다음 시퀀스번호 생성, currval : 현재시퀀스 번호 보여줌
select s_seq.nextval from dual;
select emp_seq.nextval from dual;
select emp_seq.currval from dual;

update students a
set rank=(select ranks
       from (select no,rank() over(order by total desc) as ranks       
from students) b
       where b.no = a.no);
       
select * from students;       
       
select no n,rank() over(order by total desc) as ranks       
from students;




-- 타입
-- 문자형, 숫자형, 날짜형
-- char, varchar2, nchar,nvarchar2,long,clob
-- char,varchar2 : 한글문자 입력시, 3byte 사용
-- varchar2(6) : 한글2글자입력
-- nvarchar2(5) : 한글 5자리까지 입력가능 - 2byte

-- number
-- date - 초까지 입력 , timestamp-밀리세컨드 까지 입력


select '홍길동' from dual;

-- length 문자길이
select length('홍길동') from dual;

-- 이름의 길이로 역순정렬
select name, length(name) n from students
order by n desc;

-- lengthb : byte크기
select lengthb('홍길동') from dual;



select * from students;

-- 합계 200점이상이면서, 번호10이상, 50번이하이면서 이름의 2번째 자리에 e가 들어가 있는 학생을 출력하시오.
select * from students
where total>=200 and no>=10 and no<=50 and name like '_e%';

select * from students
where total>=200;

-- select * from 테이블

select * from (
select * from students
where total>=200
) where name like '_e%' and no>=30;



rollback;

select * from students;

select no,name,total,rank from students;

-- 등수함수 rank() over(기준점) 입력, no중복이 없음. 유일키, 기본키, 프라이머리 키(primary key)
select no, rank() over(order by total desc) ranks from students;
select ranks from (select no,rank() over(order by total desc) ranks from students);

select * from students;

select no,name,total,rank from students
order by total desc;


-- 수정 : update
update students a
set rank = (
select ranks from (select no, rank() over(order by total desc) ranks from students) b 
where a.no=b.no 
)
;

update students a
set rank = 1
where a.no = 101;

select * from students order by rank;



rollback;

select no,rank() over(order by total desc) as ranks from students;


update students
set rank = 1
where no = 101;



commit;
-- 사원번호가 높은순으로 등수를 생성하시오.
-- 사원번호,사원명,등수

select employee_id,rank() over(order by employee_id desc) ranks from employees;

-- employees테이블을 그대로 emp2테이블 복사생성 
create table emp2 as select * from employees;

-- rank() 실행
select rank() over(order by employee_id desc) from employees;
desc emp2;

-- rank 테이블 컬럼 추가
alter table emp2 add rank number(4) ;
desc emp2;

select * from emp2;

-- rank() 등수를 rank에 입력
update emp2 e set rank = (
select ranks from ( select employee_id,rank() over(order by employee_id desc) ranks from employees ) e2
where e.employee_id = e2.employee_id
);

select employee_id,rank from emp2
order by employee_id desc;

select * from emp2;


-- 컬럼의 순서를 변경
-- emp_name 뒤에 rank컬럼을 숨김
alter table emp2 modify EMAIL invisible;
alter table emp2 modify phone_number invisible;
alter table emp2 modify hire_date invisible;
alter table emp2 modify salary invisible;
alter table emp2 modify MANAGER_ID invisible;
alter table emp2 modify COMMISSION_PCT invisible;
alter table emp2 modify RETIRE_DATE invisible;
alter table emp2 modify DEPARTMENT_ID invisible;
alter table emp2 modify JOB_ID invisible;
alter table emp2 modify CREATE_DATE invisible;
alter table emp2 modify UPDATE_DATE invisible;

-- 컬럼을 나타남
alter table emp2 modify EMAIL visible;
alter table emp2 modify phone_number visible;
alter table emp2 modify hire_date visible;
alter table emp2 modify salary visible;
alter table emp2 modify MANAGER_ID visible;
alter table emp2 modify COMMISSION_PCT visible;
alter table emp2 modify RETIRE_DATE visible;
alter table emp2 modify DEPARTMENT_ID visible;
alter table emp2 modify JOB_ID visible;
alter table emp2 modify CREATE_DATE visible;
alter table emp2 modify UPDATE_DATE visible;



alter table emp2 modify rank invisible;

alter table emp2 modify rank visible;

select * from emp2;


-- 컬럼 삭제

desc emp2;

alter table emp2 drop column email;
alter table emp2 drop column phone_number;

alter table emp2 drop column HIRE_DATE;
alter table emp2 drop column SALARY;
alter table emp2 drop column COMMISSION_PCT;
alter table emp2 drop column RETIRE_DATE;
alter table emp2 drop column CREATE_DATE;
alter table emp2 drop column UPDATE_DATE;


select * from emp2;


select * from departments;

desc departments;


alter table emp2 add DEPARTMENT_NAME varchar2(80)
;

-- 부서명이 없음.
select * from emp2;

-- 부서명은 departments
select * from departments;

select department_id,department_name from emp2;
select department_id,department_name from departments;

-- rank() 등수를 rank에 입력
update emp2 e set rank = (
select ranks from ( select employee_id,rank() over(order by employee_id desc) ranks from employees ) e2
where e.employee_id = e2.employee_id
);

-- 부서명 입력
update emp2 e set e.department_name = (
select d from (select department_id,department_name d from departments) e2
where e.department_id = e2.department_id
);

select department_id,department_name from emp2;



select * from stu;
drop table stu;

-- 테이블 복사
create table stu as select * from students;

desc students;

alter table stu drop column rank;

-- TOTAL    NUMBER(3)    
-- AVG      NUMBER   
-- RANK     NUMBER(3)

-- total컬럼,avg컬럼 추가하시오.
alter table stu add total number(3);
alter table stu add AVG number;
alter table stu add RANK number(3);

desc stu;

alter table stu modify sdate invisible;
alter table stu modify sdate visible;

-- 

rollback;

select * from stu;

-- 합계, 평균 추가
update stu set total = kor+eng+math,avg = (kor+eng+math)/3;

--rank 입력
select * from stu;

--rank()
select no,total,rank() over (order by total desc) ranks from stu;

update stu s set rank = 
( select ranks from ( select no,rank() over(order by total desc) ranks from stu ) s2
where s.no = s2.no 
);

select * from stu;

commit;


----- 날짜 함수
-- 현재날짜 : sysdate
select sysdate from dual;
select sysdate-1 from dual;
select sysdate+30 from dual;

create table datetable (
no number(4),
predate date,
today date,
nextdate date
);

-- 회원가입 1달치, 6개월,1년
insert into datetable values(
1,sysdate-30,sysdate,sysdate+180
);

select no,predate,today 가입일,nextdate 만료일 from datetable;



select * from member;
select id,name,mdate,sysdate,round(sysdate-mdate) from member;
select id,name,mdate,sysdate,round(sysdate-mdate) from member
where sysdate >= mdate+180
;


-- 입사일 현재날짜와 입사일 몇일 지났는지 출력하시오.
-- employees, hire_date
select sysdate-hire_date, round(sysdate-hire_date) from employees;

-- 15일 이상이면 1달을 올림, 15일 미만이면 일을 초기화
select hire_date,round(hire_date,'month') from employees;

-- 일의 숫자를 1로 초기화
select hire_date,trunc(hire_date,'month') from employees;


-- 입사일,현재일 기준의 달수
select hire_date,sysdate, months_between(sysdate,hire_date) from employees;
-- months_between :  두 일자 가운데 지나간 달수를 알려줌
select hire_date,sysdate,round(months_between(sysdate,hire_date)) 달수,round(sysdate-hire_date) 일수 from employees;

-- add_months 3개월 추가
select hire_date,add_months(hire_date,3) from employees;

-- next_day : 다음주 수요일 날짜를 알려줌.
select sysdate,next_day(sysdate,'수요일') from dual;

select sysdate, next_day(sysdate,'토요일') from dual;


-- last_date : 그달의 마지막 날짜를 알려줌
select hire_date, last_day(hire_date) from employees;

select sysdate,last_day(sysdate) from dual;



-- 형변환 함수
select sysdate from dual;
select to_char(sysdate,'yyyy/mm/dd hh24:mi:ss') from dual;
select hire_date from employees;
select hire_date,to_char(hire_date,'yyyy-mm-dd') from employees;
select to_char(to_date('24/01/01'),'yyyy/mm/dd hh24:mi:ss') from dual;
select to_char('24/01/01','yyyy-mm-dd') from dual;
-- 입력의 타입:날짜형이 되어야 함.
select to_char(to_date('24/01/01'),'yyyy-mm-dd') from dual;


select * from member where id='aaa' and pw='1111';

select * from member;

update member set id='abc',pw='1111',name='이병호',email='onulee@naver.com' 
where id='Trineman';

commit;

select * from member where id='abc';


