# ADMISSION PROCESS PROJECT

students = {}
registration_count = 1


def create_registration_number():
    global registration_count

    number = "26ST" + str(registration_count).zfill(4)
    registration_count += 1
    return number


def calculate_fees(student_class):
    if 1 <= student_class <= 5:
        return 20000
    elif 6 <= student_class <= 8:
        return 30000
    elif 9 <= student_class <= 12:
        return 35000


def new_registration():
    print("==========<< NEW REGISTRATION >>==========")

    student_name = input("Enter student name: ").strip()

    while True:
        mobile = input("Enter student mobile number: ").strip()

        if mobile.isdigit() and len(mobile) == 10:
            break
        else:
            print("Please enter a valid 10-digit mobile number.")

    while True:
        email = input("Enter e-mail ID: ").strip()

        if "@" in email and "." in email:
            break
        else:
            print("Please enter a valid e-mail ID.")

    while True:
        try:
            age = int(input("Enter age: "))

            if age > 0:
                break
            else:
                print("Age must be greater than zero.")
        except ValueError:
            print("Please enter age using numbers only.")

    gender = input("Enter gender: ").strip()

    while True:
        try:
            student_class = int(input("Enter class (1 to 12): "))

            if 1 <= student_class <= 12:
                break
            else:
                print("Class must be between 1 and 12.")
        except ValueError:
            print("Please enter a valid class.")

    print("----------< PARENT'S DETAILS >----------")

    father_name = input("Enter father's name: ").strip()
    mother_name = input("Enter mother's name: ").strip()
    father_occupation = input("Enter father's occupation: ").strip()

    while True:
        parent_mobile = input("Enter parent's mobile number: ").strip()

        if parent_mobile.isdigit() and len(parent_mobile) == 10:
            break
        else:
            print("Please enter a valid 10-digit mobile number.")

    registration_number = create_registration_number()
    fees = calculate_fees(student_class)

    students[registration_number] = {
        "student_name": student_name,
        "mobile": mobile,
        "email": email,
        "age": age,
        "gender": gender,
        "class": student_class,
        "father_name": father_name,
        "mother_name": mother_name,
        "father_occupation": father_occupation,
        "parent_mobile": parent_mobile,
        "fees": fees,
        "marks": {}
    }

    print("Registration completed successfully.")
    print("Registration Number:", registration_number)
    print("Total Fees: Rs.", fees)


def display_student(registration_number):
    if registration_number not in students:
        print("Registration number not found.")
        return

    student = students[registration_number]

    print("=============<< STUDENT DETAILS >>=============")
    print("Registration Number :", registration_number)
    print("Student Name        :", student["student_name"])
    print("Mobile Number       :", student["mobile"])
    print("E-mail ID           :", student["email"])
    print("Age                 :", student["age"])
    print("Gender              :", student["gender"])
    print("Class               :", student["class"])

    print("--------------< PARENT'S DETAILS >--------------")
    print("Father's Name       :", student["father_name"])
    print("Mother's Name       :", student["mother_name"])
    print("Father's Occupation :", student["father_occupation"])
    print("Parent's Mobile     :", student["parent_mobile"])

    print("---------------- FEES ----------------")
    print("Total Fees          : Rs.", student["fees"])

    print("---------------- MARKS ----------------")

    if len(student["marks"]) == 0:
        print("Marks have not been assigned.")
    else:
        for subject in student["marks"]:
            print(subject, ":", student["marks"][subject])

    print("==============================================")


def search_details():
    print("==========<< SEARCH DETAILS >>==========")

    registration_number = input(
        "Enter registration number: "
    ).strip().upper()

    display_student(registration_number)


def assign_marks():
    print("==========<< ASSIGNING MARKS >>==========")

    registration_number = input(
        "Enter registration number: "
    ).strip().upper()

    if registration_number not in students:
        print("Registration number not found.")
        return

    while True:
        try:
            student_class = int(input("Enter class: "))

            if student_class == students[registration_number]["class"]:
                break
            else:
                print("Class does not match the student's class.")
                return

        except ValueError:
            print("Please enter class using numbers only.")

    subjects = ["CHY", "PHY", "MAT", "CSE", "ENG"]

    print("Enter marks out of 100:")

    for subject in subjects:
        while True:
            try:
                marks = float(input("Enter marks for " + subject + ": "))

                if 0 <= marks <= 100:
                    students[registration_number]["marks"][subject] = marks
                    break
                else:
                    print("Marks must be between 0 and 100.")
  
            except ValueError:
                print("Please enter marks using numbers only.")

    print("Marks for all five subjects assigned successfully.")


def information_file():
    print("==========<< INFORMATION FILE >>==========")

    if len(students) == 0:
        print("No student information is available.")
        return

    print("1. Search using registration number")
    print("2. Show every registered student")
    print("3. Back")

    choice = input("Enter your choice: ")

    if choice == "1":
        registration_number = input(
            "Enter registration number: "
        ).strip().upper()

        display_student(registration_number)

    elif choice == "2":
        for registration_number in students:
            display_student(registration_number)

    elif choice == "3":
        return

    else:
        print("Invalid choice.")


def fees_view():
    print("===============<< FEES VIEW  >>===============")
    print("Class 1 to 5  : Rs. 20,000")
    print("Class 6 to 8  : Rs. 30,000")
    print("Class 9 to 12 : Rs. 35,000")
    print("=========================================")

    registration_number = input(
        "Enter registration number to view student fees "
        "or press Enter to go back: "
    ).strip().upper()

    if registration_number == "":
        return

    if registration_number in students:
        student = students[registration_number]

        print("Student Name :", student["student_name"])
        print("Class        :", student["class"])
        print("Total Fees   : Rs.", student["fees"])
    else:
        print("Registration number not found.")


while True:
    print("")
    print("==========================================")
    print("<<         ADMISSION PROCESS            >>")
    print("==========================================")
    print("ENTER THE SERIAL NUMBER OF SERVICE YOU WANT")
    print("1. NEW REGISTRATION")
    print("2. SEARCH DETAILS")
    print("3. ASSIGN MARKS")
    print("4. INFORMATION FILE")
    print("5. FEES VIEW")
    print("6. EXIT")
    print("7. BACK")
    print("==========================================")

    service = input("Enter your choice: ")

    if service == "1":
        new_registration()

    elif service == "2":
        search_details()

    elif service == "3":
        assign_marks()

    elif service == "4":
        information_file()

    elif service == "5":
        fees_view()

    elif service == "6":
        print("Thank you for using the Admission Process System.")
        break

    elif service == "7":
        print("You are already on the main menu.")

    else:
        print("Invalid choice. Please enter a number from 1 to 7.")
