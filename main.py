# ОБЪЯВЛЕНИЕ КЛАССОВ
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_course(self, course):
        '''
        Метод добавляет новый курс в изучаемые студентом
        Входной параметр - course (название курса)
        '''
        if course:
            self.courses_in_progress.append(course)

    def finish_course(self, course):
        '''
        Метод переводит курс студента из изучаемых в уже законченные
        Входной параметр - course (название курса)
        '''
        if course in self.courses_in_progress:
            self.courses_in_progress.remove(course)
            self.finished_courses.append(course)

    def rate_lecturer(self, lecturer, course, grade = 10):
        '''
        Метод оценивания студентом результатов работы лектора за определенный курс
        Входные параметры - lecturer (лектор), course (название курса), grade (оценка (по умолчанию 10))
        Возвращает строку удачного или неудачного результата
        '''
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached and grade >=0 and grade <= 10:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
            return 'Оценка проставлена'
        else:
            return 'Ошибка! Оценка не может быть проставлена'

    def average_course_grade(self, course):
        '''
        Метод подсчета средней оценки студента за определенный курс
        Входной параметр - course (название курса)
        Результат - средняя оценка за курс
        Если такого курса у студента нет или по нему нет оценок, то метод возвращает 0.0
        '''
        if course in self.grades:
            if len(self.grades[course]):
                return round(sum(self.grades[course]) / len(self.grades[course]), 1)
        return 0.0

    def __average_rating(self):
        '''
        Private - метод подсчета средней оценки студента за все курсы,
        по которым у студента они есть
        Входных параметров нет
        Результат - общая средняя оценка
        Если у студента вообще нет оценок, то метод возвращает 0.0
        '''
        sum_rating = 0
        count_rating = 0
        if self.grades:
            for course, grades in self.grades.items():
                if grades:
                    sum_rating += self.average_course_grade(course)
                    count_rating += 1
            return round(sum_rating/count_rating, 1)
        else:
            return 0.0

    # Переопределенный метод для вывода экземпляров класса Lecturer:
    def __str__(self):
        res_string = f'Имя:{" " * 32}{self.name}\n'
        res_string += f'Фамилия:{" " * 28}{self.surname}\n'
        res_string += f'Средняя оценка за домашние задания: {self.__average_rating()}\n'
        res_string += f'Курсы в процессе изучения:{" " * 10}{str(self.courses_in_progress).strip("[]")}\n'
        res_string += f'Завершенные курсы:{" " * 18}{str(self.finished_courses).strip("[]")}'
        return res_string

    # Переопределенные методы для сравнения экземпляров класса Student:
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

    def add_course(self, course):
        '''
        Метод добавляет новый курс для преподавателя
        Входной параметр - course (название курса)
        '''
        if course:
            self.courses_attached.append(course)

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_course_grade(self, course):
        '''
        Метод подсчета средней оценки лектора за определенный курс
        Входной параметр - course (название курса)
        Результат - средняя оценка по преподаваемому курсу
        Если такого курс лектор не ведет или по нему нет оценок, то метод возвращает 0.0
        '''
        if course in self.grades:
            if len(self.grades[course]):
                return round(sum(self.grades[course]) / len(self.grades[course]), 1)
        return 0.0

    def __average_rating(self):
        '''
        Private - метод подсчета средней оценки лектора за все курсы, которые он ведет
        Входных параметров нет
        Результат - общая средняя оценка
        Если у лектора вообще нет оценок, то метод возвращает 0.0
        '''
        sum_rating = 0
        count_rating = 0
        if self.grades:
            for course, grades in self.grades.items():
                if grades:
                    sum_rating += self.average_course_grade(course)
                    count_rating += 1
            return round(sum_rating/count_rating, 1)
        else:
            return 0.0

    # Переопределенный метод для вывода экземпляров класса Lecturer:
    def __str__(self):
        return f'Имя:{" " * 22}{self.name}\nФамилия:{" " * 18}{self.surname}\nСредняя оценка за лекции: {self.__average_rating()}'

    # Переопределенные методы для сравнения экземпляров класса Lecturer:
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
        '''
        Метод оценивания студента за определенный курс
        Входные параметры - student (студент), course (название курса), grade (оценка (по умолчанию 10))
        Возвращает строку удачного или неудачного результата
        '''
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
            return 'Оценка проставлена'
        else:
            return 'Ошибка! Оценка не может быть проставлена'

    # Переопределенный метод для вывода экземпляров класса Reviewer:
    def __str__(self):
        return f'Имя:     {self.name}\nФамилия: {self.surname}'

#======================================================================================================================
# ИСПОЛНЯЕМЫЙ КОД

# Поскольку у студентов и лекторов одинаковый словарь grades и одинаковый метод подсчета
# средних оценок за курс average_course_grade, то вместо двух функций достаточно одной.
# Правда функция (average_course_rating) выдаст результат даже, если в списке будут и лекторы и студенты вместе,
# хотя это маловероятно при использовании баз данных.
# Можно организовать проверку на однородность списка, как то:
def list_test(list_of_members):
    '''
    Функция проверяет состоит ли список list_of_members только из лекторов или только из студентов
    Входные параметры - list_of_members (список экземпляров какого-то класса)
    Результат - True  или False
    '''
    member = list_of_members[0]
    if isinstance(member, Student):
        for member in list_of_members:
            if not isinstance(member, Student):
                return False
    elif isinstance(member, Lecturer):
        for member in list_of_members:
            if not isinstance(member, Lecturer):
                return False
    else:
        return False
    return True

def average_course_rating(list_of_members, course):
    '''
    Функция подсчета средней оценки лекторов или студентов за определенный курс
    Входные параметры - list_of_members (список студентов или список лекторов), course (название курса)
    Результат - общая средняя оценка за определенный курс
    Если оценок или курсов не найдено, то функция возвращает 0.0
    '''
    if not list_test(list_of_members):
        return 'Ошибка: задан неверный список!'
    sum_grades = 0
    count_grades = 0
    for member in list_of_members:
        if course in member.grades.keys() and member.grades[course]:
            sum_grades += member.average_course_grade(course)
            count_grades += 1
    if count_grades:
        return round(sum_grades / count_grades, 1)
    else:
        return 0.0

# Предметы: 'Python', 'GIT', 'SQL', 'Jawa', 'C++', 'Дизайн', 'История КПСС'
# Студенты:
student1 = Student('Пьер', 'Безухов', 'male')
student1.courses_in_progress = ['Python', 'GIT', 'SQL', 'Jawa']
student1.finished_courses = ['C++', 'Дизайн']
student1.grades = {'C++':[4, 8, 9], 'Дизайн':[10, 9], 'Python':[6, 8, 7], 'GIT':[7, 10, 10]}
student2 = Student('Андрей', 'Болконский', 'male')
student2.courses_in_progress = ['GIT', 'SQL', 'Jawa', 'C++', 'Дизайн']
student2.finished_courses = ['История КПСС']
student2.grades = {'История КПСС':[2, 2, 8], 'Дизайн':[6, 9], 'SQL':[9, 8, 10], 'C++':[7, 9]}
student3 = Student('Наташа', 'Ростова', 'female')
student3.courses_in_progress = ['Python', 'GIT', 'История КПСС']
student3.finished_courses = ['Jawa', 'C++', 'Дизайн']
student3.grades = {'Jawa':[9, 9, 9], 'Дизайн':[10, 5], 'История КПСС':[5, 5, 6], 'C++':[10, 10], 'GIT':[9, 10]}
student4 = Student('Элен', 'Курагина', 'female' )
student4.courses_in_progress = ['Python', 'GIT', 'История КПСС']
# student4.finished_courses = ['Jawa', 'C++', 'Дизайн']
# student4.grades = {'Jawa':[9, 9, 9], 'Дизайн':[10, 5], 'История КПСС':[5, 5, 6], 'C++':[10, 10], 'GIT':[9, 10]}
students_list = [student1, student2, student3, student4]
# Лекторы:
lect1 = Lecturer('Tom', 'Cruise')
lect1.courses_attached = ['Python', 'GIT', 'SQL', 'Jawa']
lect1.grades = {'SQL':[8, 9, 9], 'GIT':[10, 9], 'Python':[7, 7, 6], 'Jawa':[10, 8, 8]}
lect2 = Lecturer('Harrison', 'Ford')
lect2.courses_attached = ['C++', 'Дизайн', 'История КПСС']
lect2.grades = {'C++':[7, 10, 9], 'Дизайн':[], 'История КПСС':[3, 4, 3]}
lect3 = Lecturer('Harry', 'Potter')
# lect3.courses_attached = ['C++', 'Дизайн', 'История КПСС']
# lect3.grades = {'C++':[7, 10, 9], 'Дизайн':[10, 10], 'История КПСС':[3, 4, 3]}
lecturers_list = [lect1, lect2, lect3]
# Рецензенты:
rev1 = Reviewer('Clint', 'Eastwood')
rev1.courses_attached = ['Python', 'GIT', 'Дизайн', 'Jawa']
rev2 = Reviewer('Tom', 'Hanks')
rev2.courses_attached = ['Python', 'GIT', 'C++', 'SQL', 'История КПСС']

# ТЕСТИРОВАНИЕ

print('=' * 30)
print('Проставление оценок:')
print(rev1.rate_student(student1, 'Python', 8))
print(rev2.rate_student(student2, 'История КПСС', 4))
print(student3.rate_lecturer(lect1, 'GIT', 9))
print(student4.rate_lecturer(lect2, 'C++'))
print(student2.rate_lecturer(rev1, 'Jawa', 6))
print('=' * 30)

# Добавление нового предмета и перемещение предмета в уже изученные:
student2.add_course('Python')
student2.finish_course('SQL')

print('Вывод экземпляров классов:')
print('Лектор:')
print(lect1)
print('=' * 30)
print('Рецензент:')
print(rev2)
print('=' * 30)
print('Студент:')
print(student2)
print('=' * 30)
print('Студент:')
print(student3)
print('=' * 30)

print('Сравнение студентов и лекторов:')
print('lect1 > lect2 -', lect1 > lect2)
print('lect1 < lect2 -', lect1 < lect2)
print('lect1 == lect2 -', lect1 == lect2)
print('student1 == student2 -', student1 == student2)
print('student1 != student2 -', student1 != student2)
print('student1 > student2 -', student1 > student2)
print('student1 <= student2 -', student1 <= student2)
print('=' * 30)

print('Вывод средних оценок за курс:')
course = 'Дизайн'
print(f'Средняя оценка лекторов за курс {course}: {average_course_rating(lecturers_list, course)}')
print(f'Средняя оценка студентов за курс {course}: {average_course_rating(students_list, course)}')
course = 'C++'
print(f'Средняя оценка лекторов за курс {course}: {average_course_rating(lecturers_list, course)}')
print(f'Средняя оценка студентов за курс {course}: {average_course_rating(students_list, course)}')
print('=' * 30)


