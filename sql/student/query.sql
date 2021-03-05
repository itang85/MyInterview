# 每个学生倒叙排序
select info.name name, avg(grade.grade) avg, sum(grade.grade) sum
from student_grade grade
         left join student_info info on grade.user_id = info.id
group by grade.user_id
order by sum desc;

# 每一科倒叙排序
select grade.subject, avg(grade.grade) avg, sum(grade.grade) sum
from student_grade grade
         left join student_info info on grade.user_id = info.id
group by grade.subject
order by avg desc;

# 数据库写一个查询数学成绩前三的学生信息
select i.name, g.subject, g.grade
from student_grade g
         left join student_info i on g.user_id = i.id
# group by i.name, g.subject, g.grade
having g.subject = "math"
order by g.grade desc
limit 3;


# 10分钟内的数据
select *
from student_grade
where create_time > now() - interval 10 minute


# 科目出现三次
select g.subject
from student_grade g
         left join student_info i on g.user_id = i.id
group by g.subject
having count(g.subject) > 3
order by g.create_time desc;


select *
from student_info i
where i.age > 10
  and i.age < 20


select i.name, grade, (select avg(sg.grade) from student_grade sg where sg.subject = "math") as ag
from student_grade
         join student_info i on user_id = i.id
where subject = "math"
  and grade > (select avg(sg.grade) from student_grade sg where sg.subject = "math")


select t.user_id, t.subject, t.grade, t1.avgScore
from student_grade t
         left join (select subject, avg(grade) as avgScore from student_grade group by subject) t1
                   on t.subject = t1.subject
where t.subject="math" and t.grade > t1.avgScore;
