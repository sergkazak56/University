class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_course(self, course_name):
        if course_name:
            self.courses_in_progress.append(course_name)

    def finish_course(self, course_name):
        if course_name in self.courses_in_progress:
            self.finished_courses.append(self.courses_in_progress.pop(course_name))

    def rate_lecturer(self, lecturer, course, grade = 10):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached and grade >=0 and grade <= 10:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
            return 'Оценка проставлена'
        else:
            return 'Ошибка! Оценка не может быть проставлена'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def add_course(self, course_name):
        if course_name:
            self.courses_attached.append(course_name)

    # def rate_hw(self, student, course, grade):
    #     if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress and grade >=0 and grade <= 10:
    #         if course in student.grades:
    #             student.grades[course] += [grade]
    #         else:
    #             student.grades[course] = [grade]
    #     else:
    #         return 'Ошибка'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_student(self, student, course, grade = 10):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
            return 'Оценка проставлена'
        else:
            return 'Ошибка! Оценка не может быть проставлена'

s1 = Student('Guy1', 'Surname1', 'male')
s1.add_course('Jawa')
s2 = Student('Guy2', 'Surname2', 'male')
s2.add_course('SQL')
s3 = Student('Guy3', 'Surname3', 'male')
s4 = Student('Girl1', 'Surname4', 'female')
l1 = Lecturer('Tom', 'Cruise')
l2 = Lecturer('Harrison', 'Ford')
l1.add_course('Python')
l1.add_course('SQL')
l1.add_course('Jawa')
l2.add_course('Jawa')
l2.add_course('C++')
l2.add_course('Дизайн')
r1 = Reviewer('Clint', 'Eastwood')
r1.add_course('Jawa')
r1.add_course('C++')
r1.add_course('Дизайн')
r2 = Reviewer('Tom', 'Hanks')
print(s1.rate_lecturer(l1, 'Jawa', 8))
print(s1.rate_lecturer(l2, 'C++'))
print(l1.grades)
print(l2.grades)
print(r1.rate_student(s1, 'Jawa', 5))
print(r1.rate_student(s2, 'SQL', 8))
print(s1.grades)
print(s2.grades)
