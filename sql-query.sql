-- ������ �������� � ����.
select s.student_name, sg.group_name from students s , s_groups sg 
where s.s_group_id = sg.group_id and sg.group_name = '��-04' ;

-- ������ �������� � ���� � ��������.
select s.student_name as �������, g.grade as ������, s2.subject_name as ������� from grades g left join students s
on g.student_id = s.id
left join s_groups sg2 
on s.s_group_id = sg2.group_id 
left join subjects s2 
on g.sub_id = s2.s_id 
where sg2.group_name = '��-04'
and s2.subject_name = 'ʳ��������'
;

--������ �����, �� ����� �������.
select s.student_name as �������, s2.subject_name as �������
from students s, subjects s2
where s.student_name = '�������� ��������';

--5 �������� �� ��������� ������� ����� � ��� ��������.
select s2.student_name, avg(g.grade) as av from grades g , students s2 
where s2.id  = g.student_id 
group by s2.student_name
order by av DESC
limit 5
;

--1 ������� �� �������� ������� ����� � ������ ��������.
select s2.student_name,  avg(g.grade) as av, s4.subject_name 
from grades g left join students s2
on g.sub_id = s2.id 
left join subjects s4
on g.sub_id = s4.s_id 
where s4.subject_name = '�������'
group by s2.student_name, s4.subject_name 
;

--������� ��� � ���� �� ������ ��������.
select sg.group_name, s2.subject_name, avg(g2.grade) as �������_���
from grades g2 left join students s
on g2.student_id = s.id
left join s_groups sg 
on s.s_group_id = sg.group_id
left join subjects s2 
on g2.sub_id = s2.s_id 
where sg.group_name = '���-01' and s2.subject_name = 'Գ����'
group by sg.group_name, s2.subject_name 
order by �������_���;

--������� ���, ���� ������� ��������.
select avg(g2.grade) as average_grade, t2.teacher_name from grades g2 left join subjects s2 
on g2.sub_id = s2.s_id 
left join teachers t2 
on s2.t_id = t2.id
where t2.teacher_name = '������ ���������'
group by t2.teacher_name
;

--������� ��� � ������. � �� ����� ���� ��������.
select avg(g2.grade) as average_grade, t2.teacher_name, s2.subject_name from grades g2 left join subjects s2 
on g2.sub_id = s2.s_id 
left join teachers t2 
on s2.t_id = t2.id
where t2.teacher_name = '��� ��������� ����'
group by t2.teacher_name, s2.subject_name 
;

--������ �����, �� �������� ���� ��������. � ������� ���, ���� �������� ������� ��������.
select avg(g2.grade) as average_grade, t2.teacher_name, s2.subject_name, s3.student_name from grades g2 left join subjects s2 
on g2.sub_id = s2.s_id 
left join teachers t2 
on s2.t_id = t2.id
left join students s3 
on g2.student_id = s3.id 
where t2.teacher_name = '���������� ���������' and s3.student_name = '������ �������'
group by t2.teacher_name, s2.subject_name, s3.student_name 
;

--������ �������� � ���� � �������� �� ���������� ������.
select distinct s.student_name, s2.subject_name, g2.grade,sg.group_name,g2.g_date
from grades g2 left join students s
on g2.student_id = s.id
left join s_groups sg 
on s.s_group_id = sg.group_id
left join subjects s2 
on g2.sub_id = s2.s_id 
where sg.group_name = '���-01' and s2.subject_name = 'Գ����'

;


