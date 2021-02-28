create table if not exists `student_info`(
  `id` int unsigned auto_increment,
  `name` varchar(100) not null,
  `age` int unsigned,
  `create_time` date,
  primary key (`id`)
)engine=InnoDB default charset=utf8;

# drop table student_grade;

create table if not exists `student_grade`(
  `id` int unsigned auto_increment,
  `subject` varchar(100) not null,
  `grade` decimal(6, 2) unsigned,
  `create_time` date,
  primary key (`id`)
)engine=InnoDB default charset=utf8;

alter table student_info modify create_time datetime default current_timestamp comment '创建时间';
alter table student_grade modify create_time datetime default current_timestamp comment '创建时间';
alter table student_info add update_time datetime default current_timestamp on update current_timestamp comment '修改时间时间';
alter table student_grade add update_time datetime default current_timestamp on update current_timestamp comment '修改时间时间';

alter table student_grade add user_id int unsigned comment '学生';

alter table student_grade add foreign key user_id(user_id) references student_info(id);
