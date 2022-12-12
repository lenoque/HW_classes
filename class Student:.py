

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}  

    def average_rating(self):
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        if all_grades:
            return sum(all_grades) / len(all_grades)
        else:
            return 0

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and 1 <= grade <= 10:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]

    def __eq__(self, other):
        return self.average_rating() == other.average_rating()
    
    def __lt__(self, other):
        return self.average_rating() < other.average_rating()

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.average_rating()} \nКурсы в процессе изучения: {self.courses_in_progress} \nЗавершенные курсы: {self.finished_courses}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'

class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    
    def average_rating(self):
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        if all_grades:
            return sum(all_grades) / len(all_grades)
        else:
            return 0
    
    def __eq__(self, other):
        return self.average_rating() == other.average_rating()
    
    def __lt__(self, other):
        return self.average_rating() < other.average_rating()

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average_rating()}'

class Reviewer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress and 1 <= grade <= 10:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'        


student_1 = Student('Elena', 'Semenova', 'female')
student_1.finished_courses = ['Git']
student_1.courses_in_progress = ['Python']

student_2 = Student('Andrey', 'Petrov', 'male')
student_2.courses_in_progress = ['Git', 'Python']


lecturer_1 = Lecturer('Timur', 'Timurovich')
lecturer_1.courses_attached = ['Python']

lecturer_2 = Lecturer('Aleksandr', 'Aleksandrovich')
lecturer_2.courses_attached = ['Git', 'Python']

reviewer_1 = Reviewer('Olga', 'Olegovna')
reviewer_1.courses_attached = ['Python']

reviewer_2 = Reviewer('Aleksandra', 'Aleksandrovna')
reviewer_2.courses_attached = ['Git']

reviewer_1.rate_hw(student_1, 'Python', 2)
reviewer_1.rate_hw(student_2, 'Python', 10)

reviewer_2.rate_hw(student_2, 'Git', 10)

print(student_1)
print(student_2)
print(student_1 > student_2, student_1 == student_2)


student_1.rate_lecturer(lecturer_1,'Python', 10)
student_2.rate_lecturer(lecturer_2,'Git', 8)
student_2.rate_lecturer(lecturer_1, 'Python', 6)


print(lecturer_1)
print(lecturer_2)
print(lecturer_2 > lecturer_1, lecturer_2 == lecturer_1)
