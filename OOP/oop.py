students_list = []
lecturers_list = []

class Student:
    def __init__(self, name, surname, gender=None):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        students_list.append(self)

    def add_finished_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course_name, grade):
        if isinstance(lecturer, Lecturer) and course_name in lecturer.courses_attached \
                and course_name in self.courses_in_progress and 1 <= grade <= 10:
            lecturer.grades += [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        grades_count = 0
        overall_grade = 0
        for grades in self.grades.values():
            if len(grades) > 0:
                for grade in grades:
                    overall_grade += grade
                    grades_count += 1
                return overall_grade / grades_count
            else:
                return 0

    def __str__(self):
        return f"Имя: {self.name} \n" \
               f"Фамилия: {self.surname} \n" \
               f"Среднняя оценка за лекции: {round(self.average_grade(), 2)} \n" \
               f"Курсы в процессе изучения: {', '.join(map(str, self.courses_in_progress))} \n" \
               f"Завершенные курсы: {', '.join(map(str, self.finished_courses))}"

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_grade() < other.average_grade()
        else:
            return 0

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []
        lecturers_list.append(self)

    def average_grade(self):
        overall_grade = 0
        if len(self.grades) > 0:
            for grade in self.grades:
                overall_grade += grade
            return overall_grade / len(self.grades)
        else:
            return 0

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() < other.average_grade()
        else:
            return 0

    def __str__(self):
        return f"Имя: {self.name} \n" \
               f"Фамилия: {self.surname} \n" \
               f"Среднняя оценка за лекции: {round(self.average_grade(), 2)}"

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f"Имя: {self.name} \n" \
               f"Фамилия: {self.surname}"

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

def average_grade_all_lecturers(lecturers_list, course_name):
    lecturers_count = 0
    all_lecturers_average_grade = 0
    for lecturer in lecturers_list:
        if isinstance(lecturer, Lecturer) and course_name in lecturer.courses_attached:
            all_lecturers_average_grade += lecturer.average_grade()
            lecturers_count += 1
    if lecturers_count == 0:
        return 'Ошибка'
    return round(all_lecturers_average_grade / lecturers_count, 2)

def average_grade_all_students(students_list, course_name):
    students_count = 0
    all_students_average_grade = 0
    for student in students_list:
        if isinstance(student, Student) and course_name in student.courses_in_progress:
            all_students_average_grade += student.average_grade()
            students_count += 1
    if students_count == 0:
        return 'Ошибка'
    return round(all_students_average_grade / students_count, 2)

one_student = Student('Иван', 'Головачев')
one_student.courses_in_progress += ['Python']
one_student.courses_in_progress += ['Git']
one_student.add_finished_courses('Введение в программирование')

second_student = Student('Валерия', 'Воеводина')
second_student.courses_in_progress += ['Python']
second_student.courses_in_progress += ['Git']
second_student.add_finished_courses('Введение в программирование')

reviewer = Reviewer("Иван", "Иванов")
reviewer.courses_attached += ['Python']
reviewer.courses_attached += ['Git']

reviewer.rate_hw(one_student, 'Python', 10)
reviewer.rate_hw(one_student, 'Python', 7)
reviewer.rate_hw(one_student, 'Python', 9)
reviewer.rate_hw(one_student, 'Git', 8)
reviewer.rate_hw(one_student, 'Git', 7)
reviewer.rate_hw(one_student, 'Git', 9)

reviewer.rate_hw(second_student, 'Python', 8)
reviewer.rate_hw(second_student, 'Python', 9)
reviewer.rate_hw(second_student, 'Python', 10)
reviewer.rate_hw(second_student, 'Git', 8)
reviewer.rate_hw(second_student, 'Git', 7)
reviewer.rate_hw(second_student, 'Git', 9)

one_lecturer = Lecturer('Олег', 'Булыгин')
one_lecturer.courses_attached += ['Python']

second_lecturer = Lecturer('Александр', 'Бардин')
second_lecturer.courses_attached += ['Python']

one_student.rate_lecturer(one_lecturer, 'Python', 7)
one_student.rate_lecturer(one_lecturer, 'Python', 8)
one_student.rate_lecturer(one_lecturer, 'Python', 6)
second_student.rate_lecturer(one_lecturer, 'Python', 9)
second_student.rate_lecturer(one_lecturer, 'Python', 8)
second_student.rate_lecturer(one_lecturer, 'Python', 7)

one_student.rate_lecturer(second_lecturer, 'Python', 8)
one_student.rate_lecturer(second_lecturer, 'Python', 9)
one_student.rate_lecturer(second_lecturer, 'Python', 7)
second_student.rate_lecturer(second_lecturer, 'Python', 8)
second_student.rate_lecturer(second_lecturer, 'Python', 6)
second_student.rate_lecturer(second_lecturer, 'Python', 9)

print(one_lecturer)
print(reviewer)
print(one_student)
print(one_student < second_student)
print(second_lecturer < one_lecturer)
print(average_grade_all_lecturers(lecturers_list, 'Python'))
print(average_grade_all_students(students_list, 'Python'))


