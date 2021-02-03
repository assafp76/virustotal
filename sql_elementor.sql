1.	Employee question - you have the following tables: 
-	employees: employee_id, first_name, last_name, hire_date, salary, manager_id, department_id
-	departments: department_id, department_name, location_id

We would like to know for each department top earning employee, salary, difference
from the second earning employee.

with rank_emp as
(
    select employee_id,employee_id, first_name, last_name,salary,department_id,
            rank() over ( partition by department_id order by salary desc) as r
    from employees    
)

select 
a2.department_name, a1.first_name, a1.last_name, a1.salary, (a1.salary - a11.salary) as diff 
from 
(select top 1 * from rank_emp where r = 1) a1 
inner join (select top 1 * from rank_emp where r = 2) a11
on a1.department_id = a11.department_id 
inner join departments a2
on a1.department_id = a2.department_id



2.	Site visiting question - you have the following tables:
-	site_visitors : date, site, number of visitors 
-	promotion dates : start_date, end_date, site, promotion_code

We would like to know what percent of the site traffic was on promotion dates 

select 
sum(case when a2.promotion_code is not null then a1.'number of visitors' else 0 end )*100/sum(a1.'number of visitors') 
as percent
from 
site_visitors a1
left outer join promotion_dates a2
on a1.site = a2.site and a1.date >= a2.start_date and a1.date <= a2.end_date

