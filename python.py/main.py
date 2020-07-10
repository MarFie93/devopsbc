
#
#
# student_1 = Student("Emerson", 123)
# student_1.enrol("DevOps")
# print(vars(student_1))
#
# student_2 = Student("Maria", 1793)
# student_2.enrol("No idea")
# print(vars(student_2))
#
# student_3 = Student("gobbledegook", 123)
# student_3.enrol("Hoping for the best")
# student_3.enrol("Python")
# print(vars(student_3))

from student import Student
from course import Course

joe = Student("Joe, 5")
mary = Student("Mary, 1")

devops = Course("DevOps", 35)

joe.enrol(devops)

print("Student=", vars(joe), ','.join(joe.courses))
print("Student=", vars(mar))
print("Course=", vars(devops))