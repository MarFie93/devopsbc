from student import Student
from student import Department
from student import Course

student_1 = Student("John Rambo", 1234)
print(student_1.name)
print(student_1.number)

department_1 = Department("IT", 222)
print(department_1.name)
print(department_1.code)
department_2 = Department("Marketing", 3)
department_3 = Department("Sales", 4)

course_1 = Course("Devops", 333, department_1)
print(vars(course_1))
print(course_1.name)
print(course_1.department.name)
print(course_1.department.code)
course_2 = Course("Python", 4, department_1)
course_3 = Course("SEO", 5, department_2)
course_4 = Course("CRM - Salesforce", 6, department_3)
