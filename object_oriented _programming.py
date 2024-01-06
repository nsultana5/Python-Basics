#Real world problem (inheritance)

class Person:                                                    #parent class
    def __init__(self,name,age,address):
        self.name=name 
        self.age=age 
        self.address=address 

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address:{self.address}")


class Student(Person):                                             #child class                              
    def __init__(self,name,age,address,student_id):
        super().__init__(name,age,address)
        self.student_id=student_id
        self.courses=[]
    def enroll(self,course):
        self.courses.append(course)
        print(f"{self.name} is enrolled in {self.courses}")

    def display_info(self):
        print(f"Student Information:")
        super().display_info()
        print(f"Student ID: {self.student_id}")
        if self.courses:
            print(f"Enrolled Courses")
            for course in self.courses:
                print(f"-{course}")


class Teacher(Person):                                              #another child class
    def __init__(self,name,age,address,employee_id):
        super().__init__(name,age,address)
        self.employee_id=employee_id
        self.teaching_courses=[]

    def assign_course(self,course):
        self.teaching_courses.append(course)
        print(f"{self.name} is assigned to teach {course}")

    def display_info(self):
        print(f"Teacher Information:")
        super().display_info()
        print(f"Employee ID: {self.employee_id}")
        if self.teaching_courses:
            print("Teaching Courses:")
            for course in self.teaching_courses:
                print(f"- {course}")

person1=Person("Nigar",35, "123 Main St")
person2=Person("Ruhul",37, "123 Jerry Drive")


student1=Student("Shiethi",13,"Jerry Drive", "s123")
student2=Student("Thiethi",5,"Jerry Drive","s345")

teacher1=Teacher("Ripon",39,"Kaligonj","e123")
teacher2=Teacher("Sumon",45,"kaligonj","e456")

person1.display_info()
print("\n")


student1.display_info()
student1.enroll("Math 101")
student1.enroll("History 201")
print("\n")

teacher1.display_info()
teacher1.assign_course("Computer Science 301")
teacher1.assign_course("Physics 202")
print("\n")


#polymorphism: Display information for different types of people
people=[person1,person2,student1,teacher1,student2,teacher2]
for person in people:
    person.display_info()
    print("\n")