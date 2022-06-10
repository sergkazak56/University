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

    def __average_rating(self):
        sum_rating = 0
        count_rating = 0
        if self.grades:
            for grade_list in self.grades.values():
                sum_rating += sum(grade_list)
                count_rating += len(grade_list)
        if count_rating:
            return round(sum_rating/count_rating, 1)
        else:
            return 0.0

    def __str__(self):
        res_string =  f'Имя:{" " * 32}{self.name}\n'
        res_string += f'Фамилия:{" " * 28}{self.surname}\n'
        res_string += f'Средняя оценка за домашние задания: {self.__average_rating()}\n'
        res_string += f'Курсы в процессе изучения:{" " * 10}{str(self.courses_in_progress).strip("[]")}\n'
        res_string += f'Завершенные курсы:{" " * 18}{str(self.finished_courses).strip("[]")}'
        return res_string

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.__average_rating() < other.__average_rating()
        else:
            print('Ошибка: сравнение с экземпляром другого класса')

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.__average_rating() == other.__average_rating()
        else:
            print('Ошибка: сравнение с экземпляром другого класса')

    def __le__(self, other):
        if isinstance(other, Student):
            return self.__average_rating() <= other.__average_rating()
        else:
            print('Ошибка: сравнение с экземпляром другого класса')

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

    def __average_rating(self):
        sum_rating = 0
        count_rating = 0
        if self.grades:
            for grade_list in self.grades.values():
                sum_rating += sum(grade_list)
                count_rating += len(grade_list)
        if count_rating:
            return round(sum_rating/count_rating, 1)
        else:
            return 0.0

    def __str__(self):
        return f'Имя:{" " * 22}{self.name}\nФамилия:{" " * 18}{self.surname}\nСредняя оценка за лекции: {self.__average_rating()}'

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.__average_rating() < other.__average_rating()
        else:
            print('Ошибка: сравнение с экземпляром другого класса')

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.__average_rating() == other.__average_rating()
        else:
            print('Ошибка: сравнение с экземпляром другого класса')

    def __le__(self, other):
        if isinstance(other, Lecturer):
            return self.__average_rating() <= other.__average_rating()
        else:
            print('Ошибка: сравнение с экземпляром другого класса')

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

    def __str__(self):
        return f'Имя:     {self.name}\nФамилия: {self.surname}'

# Предметы: 'Python', 'GIT', 'SQL', 'Jawa', 'C++', 'Дизайн', 'История КПСС'
# Студенты:
student1 = Student('Guy1', 'Surname1', 'male')
student1.courses_in_progress = ['Python', 'GIT', 'SQL', 'Jawa']
student1.finished_courses = ['C++', 'Дизайн']
student1.grades = {'C++':[4, 8, 9], 'Дизайн':[10, 9], 'Python':[6, 8, 7], 'GIT':[7, 10, 10]}
student2 = Student('Guy2', 'Surname2', 'male')
student2.courses_in_progress = ['GIT', 'SQL', 'Jawa', 'C++', 'Дизайн']
student2.finished_courses = ['История КПСС']
student2.grades = {'История КПСС':[2, 2, 8], 'Дизайн':[6, 9], 'SQL':[9, 8, 10], 'C++':[7, 9]}
student3 = Student('Girl1', 'Surname3', 'female')
student3.courses_in_progress = ['Python', 'GIT', 'История КПСС']
student3.finished_courses = ['Jawa', 'C++', 'Дизайн']
student3.grades = {'Jawa':[9, 9, 9], 'Дизайн':[10, 5], 'История КПСС':[5, 5, 6], 'C++':[10, 10], 'GIT':[9, 10]}
student4 = Student('Girl2', 'Surname4', 'female' )
student4.courses_in_progress = ['Python', 'GIT', 'История КПСС']
student4.finished_courses = ['Jawa', 'C++', 'Дизайн']
student4.grades = {'Jawa':[9, 9, 9], 'Дизайн':[10, 5], 'История КПСС':[5, 5, 6], 'C++':[10, 10], 'GIT':[9, 10]}
# Лекторы:
lect1 = Lecturer('Tom', 'Cruise')
lect1.courses_attached = ['Python', 'GIT', 'SQL', 'Jawa']
lect1.grades = {'SQL':[8, 9, 9], 'GIT':[10, 9], 'Python':[7, 7, 6], 'Jawa':[10, 8, 8]}
lect2 = Lecturer('Harrison', 'Ford')
lect2.courses_attached = ['C++', 'Дизайн', 'История КПСС']
lect2.grades = {'C++':[7, 10, 9], 'Дизайн':[10, 10], 'История КПСС':[3, 4, 3]}
lect3 = Lecturer('Harry', 'Potter')
# lect3.courses_attached = ['C++', 'Дизайн', 'История КПСС']
# lect3.grades = {'C++':[7, 10, 9], 'Дизайн':[10, 10], 'История КПСС':[3, 4, 3]}
# Рецензенты:
rev1 = Reviewer('Clint', 'Eastwood')
rev1.courses_attached = ['Python', 'GIT', 'Дизайн', 'Jawa']
rev2 = Reviewer('Tom', 'Hanks')
rev2.courses_attached = ['Python', 'GIT', 'C++', 'SQL', 'История КПСС']
# print(lect1)
# print('=============================')
# print(lect2)
# print('=============================')
# print(lect3)
# print('=============================')
print(student1)
print('=============================')
print(student2)
print('=============================')
print(student3)
print('=============================')
print(student4)
print(student1 > student2)
print('=============================')
print(student1 < student2)
print('=============================')
print(student1 == student2)
print('=============================')
print(student3 == student4)
print('=============================')
print(student3 != student4)
print('=============================')
print(student3 <= student4)
print('=============================')
print(student3 >= student4)
print('=============================')
