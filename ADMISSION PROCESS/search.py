def search_details():
    print("==========<< SEARCH DETAILS >>==========")

    registration_number = input(
        "Enter registration number: "
    ).strip().upper()

    display_student(registration_number)
