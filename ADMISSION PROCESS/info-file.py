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