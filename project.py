import os
class Course:
    last_course_id = 0 # عداد 
    valid_course_levels = ["A", "B", "C"]
    courses_data = []

    def __init__(self, course_name, course_level):
        Course.last_course_id += 1 # بداية العد لزيادة الاي دي 
        self.course_id = Course.last_course_id
        self.course_name = course_name
        
        if course_level in Course.valid_course_levels:
            self.course_level = course_level
        else:
            raise ValueError("Invalid course level")
        Course.courses_data.append(self)  ### (يتم التخزين على شكل كائن فلا يمكن الوصول للداتا الا من داخل الكلاس او يمكن الوصول لها من الخارج ولكن تكون جملة واحدة على شكل كائن)تخزين الكائن في الداتا

        

    def display_course_details():  # استعنا بالكلاس اوبجيكت للوصول للداتا 
        course_id = int(input("Enter the course ID: "))
        course = Course.search_course_by_id(course_id)
        if course:
            print("\nCourse Details:")
            print(f"Course ID: {course.course_id}")
            print(f"Course Name: {course.course_name}")
            print(f"Course Level: {course.course_level}")
        else:
            print("Course not found.")
    
    @classmethod
    def search_course_by_id(cls, course_id): ## لا يمكن الوصل للداتا الا من داخل الكلاس لذلك تحتم استخدام كلاس اوبجيكت 
        for course in cls.courses_data:
            if course.course_id == course_id:
                return course
        return None
    


    def display_all_courses():  # استعراض البيانات 
         print("\nAll Courses:")
         counter=0
         for course in Course.courses_data:
              counter+=1
              print(f"{counter} _ Course ID: {course.course_id}, Course Name: {course.course_name}, Course Level: {course.course_level}")



    def add_new_course(): # اضافة كائن من نوع كورس
        course_name = input("Enter course name: ")
        course_level = input("Select course level (A, B, or C): ")
        while course_level not in Course.valid_course_levels:
            print("Invalid input. Please select a valid course level.")
            course_level = input("Select course level (A, B, or C): ")
        course = Course(course_name, course_level)
        print("Course added successfully.")    

    
    def delete_course_by_id(): # حذف كائن من الموجود مسبقا
        course_id = int(input("Enter the course ID to delete: "))
        course = Course.search_course_by_id(course_id)
        if course:
            Course.courses_data.remove(course)
            print("Course deleted successfully.")
        else:
            print("Course not found.")
#############################################################################################33
class Student:
    last_student_id = 0
    valid_student_levels = ["A", "B", "C"]
    students_data = []

    def __init__(self, student_name, student_level):
        Student.last_student_id += 1
        self.student_id = Student.last_student_id
        self.student_name = student_name
        if student_level in Student.valid_student_levels:
            self.student_level = student_level
        else:
            raise ValueError("Invalid student level")
        self.student_courses = []
        Student.students_data.append(self)

    def add_course(self, course): 
        if self.student_level == course.course_level:
            self.student_courses.append(course)
            
        else:
            print(f"Student level ({self.student_level}) doesn't match course level ({course.course_level}). Course not added.")
            return "doesn't match"
            

    def display_student_details(self):
        print(f"Student Name: {self.student_name}")
        print(f"Student ID: {self.student_id}")
        print(f"Student Level: {self.student_level}")
        print("Courses Enrolled:")
        for course in self.student_courses:
            print(course.course_name)


def add_new_student(): ##
    student_name = input("Enter student name: ")
    student_level = input("Select student level (A, B, or C): ")
    while student_level not in Student.valid_student_levels:
        print("Invalid input. Please select a valid student level.")
        student_level = input("Select student level (A, B, or C): ")
    student = Student(student_name, student_level)
    # Student.students_data.append(student)
    print("Student Added successfully.")


def remove_student(): ##
    student_id = int(input("Enter student ID to remove: "))
    for student in Student.students_data:
        if student.student_id == student_id:
            Student.students_data.remove(student)
            print("Student deletion done successfully.")
            return
    print("User does not exist.")


def edit_student(): 
    student_id = int(input("Enter student ID to edit: "))
    for student in Student.students_data:
        if student.student_id == student_id:
            new_name = input("Enter new name: ")
            new_level = input("Select new level (A, B, or C): ")
            while new_level not in Student.valid_student_levels:
                print("Invalid input. Please select a valid student level.")
                new_level = input("Select new level (A, B, or C): ")
            student.student_name = new_name
            student.student_level = new_level
            print("Student details updated successfully.")
            return
    print("user not exist.")


def display_all_students(): 
    print("\nAll Students:")
    for student in Student.students_data:
        print(f"Student ID: {student.student_id}, Student Name: {student.student_name}, Student Level: {student.student_level}")


def create_new_course():
    course_name = input("Enter course name: ")
    course_level = input("Select course level (A, B, or C): ")
    while course_level not in Course.valid_course_levels:
        print("Invalid input. Please select a valid course level.")
        course_level = input("Select course level (A, B, or C): ")
    course = Course(course_name, course_level)
    print("Course created successfully.")


def add_course_to_student():
    student_id = int(input("Enter student ID: "))
    
    for s in Student.students_data:
        if s.student_id == student_id:
            student = s
            break
    if student:
        course_id = int(input("Enter course ID to add to the student: "))
        course = Course.search_course_by_id(course_id)
        if course:
            student.add_course(course)
            
            try :
                if "doesn't match" in student.add_course(course) :
                    pass
            except:
                print(f"Course {course.course_name} added to {student.student_name}'s courses.")
        else:
            print("Course does not exist.")
    else:
        print("Student does not exist.")



course1 = Course("Math", "A")
course2 = Course("History", "B")
course3 = Course("Englesh", "C")
course4 = Course("prgramming", "A")

student1=Student("Osama","A")
student2=Student("Rame","B")
student3=Student("Wesam","C")
student3=Student("Ahmed","C")




while True:
    print("\n works:")
    print("1. Add New Student")
    print("2. Remove Student")
    print("3. Edit Student")
    print("4. Add Course to Student")
    print("5. Display All Students")
    print("6. show avilible courses ")
    print("7. dispaly course detales ")
    print("8. Add new course ")
    print("9. remove course ")
    print("10. clear ")
    print("11. Quit")

    choice = input("Enter your choice: ")
    print('\n \n \n')
    if choice == "1":
        add_new_student()
    elif choice == "2":
        remove_student()
    elif choice == "3":
        edit_student()
    elif choice == "4" :
        add_course_to_student()
    elif choice == "5":
        display_all_students()
    elif choice == "6":
          Course.display_all_courses()
    elif choice == '7':
          Course.display_course_details()
    elif choice == "8":
        create_new_course()
    elif choice =="9":
           Course.delete_course_by_id()
    elif choice=='10':
          os.system('cls')  
    elif choice == "11":
        break
    else:
        print("Invalid choice. Please select a valid option.")


# done by Abdalrheem abo kwaik & stakoverflow :)