select * from students;

select * from students where no>=50;
select * from students where no>=90;

select * from students where no in(10,20,30)
;

select * from employees where employee_id>=120;


select * from employees where emp_name like '%a%';


select * from employees where emp_name like ':1';


select employee_id,emp_name,salary from employees where salary >= 4000 and salary <= 8000
order by salary;




