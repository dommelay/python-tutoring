# CLASS, INSTANCE, AND LOCAL VARIABLES ------------------------------------------------
class A:
    # class variables
    x = 0
    y = 7
    # instance variable
    def __init__(self, a):
        self.x = a
        A.x += 1
# print(A.x) # 0
# print(A.y) # 7
# a1 = A(3)
# print(a1.x) # 3
# print(A.x) # 1, incremented once
A.y = 9
# print(a1.y) # 9
a2 = A(5)
# print(a2.x, A.x, a2.y) # 5, 2, 9

class A:
    x = 0
    def __init__(self, a):
        self.x = a
        x = A.x + 1  
        # x is a local variable
        # print(x) # 1
a2 = A(7)
# print(a2.x, A.x) # 7, 0



# EXAMPLE: UNIVERSITY, PROFESSOR, STUDENT, COOURSE ------------------------------------------------
class University:
    def __init__(self, name):
        self.name = name
        self.student_dict = {}   # key: ID, value: student object; to find a student object based on the student_id
        self.course_dict = {}    # key: ID, value: course object; to find a course object based on the course_id
        self.staff_dict = {}   # key: ID, value: staff object; to find staff object based on the student_id
#    def __repr__(self):
#        return self.name      
class Person:
    person_count = 0  # class variable
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = None
        Person.person_count += 1  ## count each additional person added
    def get_full_name(self) -> str:
        return self.first_name + ' ' + self.last_name
class Student(Person):
    good_gpa = 3.0  # class variable
    def __init__(self, first_name: str, last_name: str, university: University, student_id: str):
        super().__init__(first_name, last_name)  # initialize the super class Person
        self.university = university
        self.student_id = student_id
        self.gpa = None
        self.courses = []
        university.student_dict[self.student_id] = self  # so we can look up the student by ID
    def enroll(self, course) -> None:
        self.courses.append(course)  # add course to student's courses
        course.add_student(self)     # add student to course's students
    def print_courses(self) -> None:
        print(f"\nCourses for {self.get_full_name()}:")
        for course in self.courses:
            print(f" - {course.get_name()}")
    def good_standing(self):
        return self.gpa >= Student.good_gpa
class Professor(Person):
    def __init__(self, first_name, last_name, university, professor_id):
        super().__init__(first_name, last_name) 
        self.university = university
        self.professor_id = professor_id
        self.courses = []  # courses taught
    def teaches(self, course):
        self.courses.append(course)  # add course to professor's courses
        course.add_professor(self)   # add professor to course's professors (calling Course method)
    def print_courses(self):
        print(f"\nCourses for {self.get_full_name()}:")
        for course in self.courses:
            print(f" - {course.get_name()}")     
class Course:
    def __init__(self, university, course_id, name):
        self.university = university
        self.course_id = course_id
        self.course_name = name
        self.students = []
        self.professors = []
        university.course_dict[self.course_id] = self  # so we can look up the course by ID
    def get_name(self) -> str:
        return self.course_name
    def add_student(self, student: Student) -> None:
        self.students.append(student)
    def add_professor(self, professor: Professor) -> None:
        self.professors.append(professor)
    def print_roster(self) -> None:
        print(f"\nStudents in {self.course_name}:")
        for student in self.students:
            print(f" - {student.get_full_name()}")
usc = University("University of Southern California")
dsci510 = Course(usc, "20221_dsci_510_32431", "Principles of Programming for Data Science")
dsci553 = Course(usc, "20221_dsci_553_32418", "Foundations and Applications of Data Mining")
john = Student("John", "Smith", usc, "1234567890")
mary = Student("Mary", "Davis", usc, "1287654390")
john.enroll(dsci510)
mary.enroll(dsci510)
mary.enroll(dsci553)

# OBJECT.METHOD(ARGS) == CLASS.METHOD(OBJ, ARGS) ------------------------------------------------
# print(dsci510.get_name()) # Principles of Programming for Data Science
# print(Course.get_name(dsci510)) # Principles of Programming for Data Science
# print(hex(id(dsci510))) # 0x10510e880 # id returns identity of object, hex converts integer to lowercase hexidecimal string
jl = Professor('JL', 'Ambite', usc, 'P12345')
jl.teaches(dsci510)              # normal method call style: object.method(args)
Professor.teaches(jl, dsci553)   # Here you can see why the self parameter is needed
# print(jl) # <__main__.Professor object at 0x10280e760>
# print(jl.get_full_name()) # JL Ambite
# print(jl.courses) # [<__main__.Course object at 0x10280e8b0>, <__main__.Course object at 0x10280e820>]
# print([ (c.course_id, c.course_name) for c in jl.courses]) # [('20221_dsci_510_32431', 'Principles of Programming for Data Science'), ('20221_dsci_553_32418', 'Foundations and Applications of Data Mining')]
ulf = Professor('Ulf', 'Hermjakob', usc, 'P12345789')
Professor.teaches(ulf,dsci510)
# print(ulf) # <__main__.Professor object at 0x102646730>
# print(ulf.courses) # [<__main__.Course object at 0x1026468b0>]

# ACCESSING AND NAVIGATING OBJECTS ------------------------------------------------
def example(usc):
    for s in usc.student_dict.values():
        s.print_courses()
    for c in usc.course_dict.values():
        c.print_roster()
# example(usc)
# print(mary.courses)
# print(usc.student_dict)       
# print(usc.student_dict['1287654390']) # <__main__.Student object at 0x1024e6760>
# print(usc.student_dict['1287654390'].first_name) # Mary
# print(usc.student_dict['1287654390'].get_full_name()) # Mary Davis
# print(usc.student_dict['1287654390'].courses) # [<__main__.Course object at 0x1045e28e0>, <__main__.Course object at 0x1045e2880>]
# print(usc.student_dict['1287654390'].courses[0]) # <__main__.Course object at 0x10255a8e0>
# print(usc.student_dict['1287654390'].courses[0].course_name) # Principles of Programming for Data Science
# print(usc.student_dict['1287654390'].courses[0].students) # [<__main__.Student object at 0x104f66790>, <__main__.Student object at 0x104f66760>]
# print(usc.student_dict['1287654390'].courses[0].students[1]) # <__main__.Student object at 0x10024e760>
# print(usc.student_dict['1287654390'].courses[0].students[1].get_full_name()) # Mary Davis
# print(mary.get_full_name(), mary) # Mary Davis <__main__.Student object at 0x1006be760>
# print("- mary's courses:", mary.courses) # - mary's courses: [<__main__.Course object at 0x1006be8e0>, <__main__.Course object at 0x1006be880>]
# for c in mary.courses:
#     print('-- course:', c.course_name, c)
#     print('--- profs:', c.professors)
#     for p in c.professors:
#         print('---- prof:', p.get_full_name(), p)
# print(mary.courses[0].professors[0].get_full_name())

