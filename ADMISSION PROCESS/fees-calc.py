def calculate_fees(student_class):
    if 1 <= student_class <= 5:
        return 20000
    elif 6 <= student_class <= 8:
        return 30000
    elif 9 <= student_class <= 12:
        return 35000