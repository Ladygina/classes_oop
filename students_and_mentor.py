import numpy as np
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []



class Lectors(Mentor):
    def __init__(self,name, surname,courses_list):
        super().__init__(name, surname)
        self.average_points = 0.0         # средняя оценка качества лекций
        self.courses_list = courses_list  # перечень курсов, которые ведут лекторы
        self.course_point ={}             # словарь оценок по ключу курса


############## task3
    def __str__(self):
        string =''
        string += 'Имя:' + self.name +"\n"
        string += 'Фамилия:'+ self.surname +"\n"
        string += 'Средняя оценка за лекции:' + str(self.average_points) + "\n"

        return  string

    def __lt__(self, other):
        flag = False
        string =''
        if self.average_points < other.average_point:
            string = self.name + self.surname + 'has less average point than'+\
                    other.name + other.surname
            flag = True
        return flag, string

    def __gt__(self, other):
        flag = False
        string =''
        if self.average_points > other.average_point:
            string = self.name + self.surname + 'has bigger average point than'+\
                    other.name + other.surname
            flag = True
        return flag, string


    def __eq__(self, other):
        flag = False
        string =''
        if self.average_points == other.average_point:
            string = self.name + self.surname + 'has equal average point than'+\
                    other.name + other.surname
            flag = True
        return flag, string

    def count_avg_point(self):
        values_points = list(self.course_point.values())
        avg = np.mean( values_points)
        self.average_points = avg


####### task1
class Student():

    def __init__(self, name, surname, gender, finished_courses_list ,courses_in_progress_list ,
                 courses_attached_list):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = finished_courses_list
        self.courses_in_progress = courses_in_progress_list
        self.courses_attached=courses_attached_list
        self.grades = {}
        self.avg_grades = 0

    ############## task3
    def __str__(self):
        string = ''
        string += 'Имя:' + self.name + "\n"
        string += 'Фамилия:' + self.surname + "\n"
        string += 'Средняя оценка за домашние задания:' + str(self.avg_grades) + "\n"
        string += 'Курсы в процессе изучения:' + str(self.courses_in_progress) + "\n"
        string += 'Завершенные курсы:' + str(self.finished_courses) + '\n'

        return string

    ############## task2
    def points_for_lectures(self, lector, course, course_grade):
            if isinstance(lector, Lectors) and course in self.finished_courses and course in lector.courses_list:
                if course in lector.course_point:
                    lector.course_point[course] += [course_grade]   # оценка курса студентами
                else:
                    lector.course_point[course] = [course_grade]
            else:
                return 'Ошибка'

    def count_avg_point(self):
        values_points = list(self.grades.values())
        avg = np.mean(values_points)
        self.avg_grades = avg

####### task1
class Reviewers(Mentor):
    def __init__(self,name, surname, courses_attached):
        super().__init__(name, surname)
        self.courses_attached= courses_attached

    ############## task3
    def __str__(self):
        string =''
        string += 'Имя:' + self.name +"\n"
        string += 'Фамилия:'+ self.surname +"\n"
        return string

    ############## task2
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]

            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


########### task4
mentor1 = Mentor('Ivan', 'Semenov')
mentor2 = Mentor('Ivanessa', 'Semenova')   # don't know why...

#_________________________________________________
lector1 = Lectors('Svetlana', 'Kuznetsova', ['math', 'history'])
lector2 = Lectors('Nadezhda', 'Kuznetsova', ['math', 'chemistry'])

#_________________________________________________

good_boy = Student('Vasya', 'Smirnov', 'male', ['math',  'chemistry','history'],
                   ['history'], ['math', 'history', 'chemistry'])
bad_boy = Student('Egor', 'Smirnov', 'male', ['history'],
                   ['math','history', 'chemistry'], ['history'])


bad_boy.points_for_lectures(lector1,'history', 6 )          # выставление оценки за лекции
good_boy.points_for_lectures(lector1,'math', 10 )

good_boy.points_for_lectures(lector2,'math', 9.9 )
#_________________________________________________
lector1.count_avg_point()
lector2.count_avg_point()
print(lector1, "\n", lector2)

#_________________________________________________
rewiewer1= Reviewers('Nikita', 'Alexeev', ['math', 'history', 'chemistry'])
rewiewer2= Reviewers('Marina', 'Alexeeva', ['math', 'history', 'chemistry'])
print(rewiewer1, "\n", rewiewer2)

rewiewer1.rate_hw(good_boy, 'history', 5.0)         # выставление оценок ревьювером
rewiewer2.rate_hw(bad_boy, 'history', 4.8)

good_boy.count_avg_point()                          # средняя оценка за домашние задания
bad_boy.count_avg_point()
print(good_boy, "\n", bad_boy)


def hw_avg_point(students_list, course_name):
    sum =0.0
    for i in range(len(students_list)):
        if isinstance(students_list[i], Student):
            sum += students_list[i].grades[course_name][0]
    avg = float(sum)/len(students_list)
    return avg

def lectores_avg_point(lectors_list, course_name):
    sum =0.0
    for i in range(len(lectors_list)):
        if isinstance(lectors_list[i], Lectors):
            sum += lectors_list[i].course_point[course_name][0]

    avg = float(sum)/len(lectors_list)
    return avg


print(hw_avg_point([good_boy, bad_boy], 'history'))
print(lectores_avg_point([lector1, lector2], 'math'))
