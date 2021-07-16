class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_attached \
                                            and course in lecturer.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def calculate_average_grade_homework(self):
        grades_lists = self.grades.values()
        all_grades = []
        for grade in grades_lists:
            all_grades += grade
            res = round(sum(all_grades) / len(all_grades), 1)
        return res

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n' \
              f'Средняя оценка за домашние задания: {self.calculate_average_grade_homework()}\n' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
              f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.calculate_average_grade_homework() < other.calculate_average_grade_homework()



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.course_grades = {}



class Lecturer(Mentor):

    def calculating_the_average(self):
        grades_lists = self.course_grades.values()
        all_grades = []

        for grade in grades_lists:
            all_grades += grade
            res = round(sum(all_grades) / len(all_grades), 1)
        return res

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за лекции: {self.calculating_the_average()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.calculating_the_average() < other.calculating_the_average()



class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached \
                                        and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res



def output_of_the_average_grade_for_the_course(list_students, course_name):
    grades_lists = []

    for student in list_students:
        for course, grades in student.grades.items():
            if course == course_name:
                grades_lists += grades

    res = f'Средняя оценка за домашние задания по всем студентам в рамках курса "{course_name}"\n' \
          f'составлет {round(sum(grades_lists) / len(grades_lists), 1)} балл(ов)'
    return res



def output_of_the_average_score_of_lecturers(list_lecturers, title_lecture_course):
    grades_lists = []

    for lecturer in list_lecturers:
        for course, grades in lecturer.course_grades.items():
            if course == course_name:
                grades_lists += grades

    res = f'Средняя оценка за лекции всех лекторов в рамках курса "{title_lecture_course}"\n' \
          f'составлет {round(sum(grades_lists) / len(grades_lists), 1)} балл(ов)'
    return res



best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
print()
print(best_student.grades)



first_student = Student('Влад', 'Мягкий', 'муж')
first_student.grades = {'Python': [7, 10, 4], 'Git': [7.5, 10, 8]}
first_student.courses_in_progress = ['Python', 'Git']
first_student.finished_courses = ['Введение в программирование']
print()
print(first_student)

second_student = Student('Андрей', 'Доронин', 'муж')
second_student.grades = {'Python': [9, 5, 7], 'Git': [8, 10, 9]}
print()
print(second_student)
print()
print(first_student < second_student)


first_lecturer = Lecturer('Тимур','Вотяков')
first_lecturer.course_grades = {'Python': [10, 8, 7], 'Git': [7, 10, 9]}
print()
print(first_lecturer)
second_lecturer = Lecturer('Павел','Соловьёв')
second_lecturer.course_grades = {'Python': [10, 9, 5], 'Git': [8, 10, 4]}
print()
print(second_lecturer)
print()
print(first_lecturer > second_lecturer)



list_students = [first_student, second_student]
course_name = 'Python'
print()
print(output_of_the_average_grade_for_the_course(list_students, course_name))



list_lecturers = [first_lecturer, second_lecturer]
title_lecture_course = 'Python'
print()
print(output_of_the_average_score_of_lecturers(list_lecturers, title_lecture_course))