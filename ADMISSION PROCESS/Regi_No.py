def create_registration_number():
    global registration_count

    number = "26ST" + str(registration_count).zfill(4)
    registration_count += 1
    return number
