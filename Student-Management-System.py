class Student:
    def __init__(self, name, rollNumber, oweDues, numPresent, att):
        self.name = name
        self.roll = rollNumber
        self.fees = oweDues
        self.numDaysPresent = numPresent
        self.att = att

def execute_Program():
    print("Enter the serial number to select the option")
    print("1. Find a Student's Record")
    print("2. Delete a student record")
    print("3. Update Student's Record")
    print("4. Print the list of all students")
    print("5. Add a New Student")
    print("Enter 0 to exit")
    x = input("\nOperation: ")

    if x == "0":
        return
    elif x == "1":
        findStudentRecords()
    elif x == "2":
        deleteRecord()
    elif x == "3":
        update_Record()
    elif x == "4":
        print_students()
    elif x == "5":
        add_Student()
    else:
        return "Error: please in numbers from 0 to 5"

#1
def findStudentRecords():
    student_finder = input("Please enter the student's first and last name: ")
    print("Name, Roll Number, Fees Due?, Days Present, Attendance")
    print(all_students[student_finder])
    continue_Process()

#2
def deleteRecord():
    global numofStudents
    student_remover = input("Please enter the student's first and last name: ")
    all_students.pop(student_remover)
    numofStudents -= 1
    print(student_remover + " has been removed from the database.")

    continue_Process()

#3
def update_Record():
    global numofStudents
    global totalDays
    global name
    global student
    student_updater = input("Please enter the student's first and last name: ")
    arr = all_students[student_updater]

    student_ID = arr[1]
    print("Student ID: " + str(student_ID))

    #update name
    update_name = input("If there is a change in name, press 1. If not, press 0: ")
    if update_name == "1":
        name = input("Change Student Name(First and Last name):  ")
        print(name)
    else:
        name = arr[0]
        print(name)

    #roll_number
    roll_number = arr[1]
    print(roll_number)

    #update fees
    update_fees = input("If there is a change in payment, press 1. If not, press 0: ")
    if update_fees == "1":
        fees_paid = input("Fee's paid (P) or Not Paid(N) (P/N): ")
        print(fees_paid)
    else:
        fees_paid = arr[2]
        print(fees_paid)

    #update present and attendance
    update_present = input("If there is a change in the number of days the student was present, press 1. If not, press 0. ")
    if update_present == "1":
        str_present = input("number of days a student was present: ")
        present = int(str_present)
        attendance = (present) / totalDays * 100
        print("Attendance Percentage: ")
        print(attendance)
    else:
        present = arr[3]
        print(present)
        attendance = (present) / totalDays * 100
        print("Attendance Percentage")
        print(attendance)

    #student removal and final update
    all_students.pop(student_updater)
    student = Student(name, roll_number, fees_paid, present, attendance)
    all_students[student.name] = [student.name, student.roll, student.fees, student.numDaysPresent, student.att]
    continue_Process()

def print_students():
    global all_students
    print("Name, Roll Number, Fees Due?, Days Present, Attendance ")
    for i in all_students:
        print(all_students[i])
    continue_Process()

def createStudent():
    global numofStudents
    global totalDays
    global name
    global student
    numofStudents += 1
    student_ID = numofStudents
    print("Student ID: " + str(student_ID))

    name = input("Enter Student Name(First and Last name):  ")
    print(name)

    roll_number = numofStudents
    print("Students Roll Number and ID number: ")
    print(roll_number)

    fees_paid= input("Fee's paid (P) or Not Paid(N) (P/N): ")
    print("Fees paid: ")
    print(fees_paid)

    str_present = input("number of days a student was present: ")
    print("Number of days student was present: ")
    print(str_present)
    present = int(str_present)
    attendance = (present)/totalDays*100
    print("Students attendance percentage:")
    print(attendance)

    student = Student(name, roll_number, fees_paid, present, attendance)


def add_Student():
    global all_students
    createStudent()
    all_students[student.name] = (student.name, student.roll, student.fees, student.numDaysPresent, student.att)
    execute_Program()

def continue_Process():
    continue_process = input("Press 1 to continue: ")
    if continue_process == "1":
        execute_Program()
    else:
        return


if __name__ == "__main__":
    option = 0
    i = 0
    j = 0
    present = 75
    money = 'P'
    totalDays = 119
    all_students = {}
    numofStudents = 0

    #Program starts here
    print("Student Database")
    print("\nEnter 1 to add student")
    print("\nEnter 0 to Exit")
    y = input("\nInput operation here: ")

    if y == "1":
        add_Student()
    elif y == "0":
        print("All done!")


