self.name = name
        self.student_number = student_number
        self.courses = []
    def enrol(self, course):
        self.courses.append(course)
class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code

class Course:
    def __init__(self, name, course_code, department):
        print("Instantiating a course")
        print(name, course_code, "Department:", vars(department))
        self.name = name
        self.course_code = course_code
        self.department = department
        self.courses = ["DevOps", "Python", "No idea", "Hoping for the best"]
        self.credits = credits()
