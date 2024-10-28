-- 주석
-- 실행단축키 : F9
-- 계정이름 앞에 c## 생략 코드
alter session set "_ORACLE_SCRIPT" = true ;


-- 사용자 생성
create user ora_user identified by 1111;

-- 권한부여 : 접근권한,리소스 권한, db생성권한
grant connect,resource,dba to ora_user;

-- 권한 해제
revoke connect,resource,dba from ora_user;

-- 사용자 계정 삭제
drop user ora_user;

create user ora_user identified by 1111;
grant connect,resource,dba to ora_user;
