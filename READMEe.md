# Admission Process Project

## Project Overview

The **Admission Process Project** is a menu-driven Python program used to register students and manage their admission information. It runs in the Python interpreter and does not require a website, database, or external library.

The program stores student records temporarily in a Python dictionary while it is running.

## Main Features

1. New student registration
2. Automatic registration number generation
3. Student and parent details storage
4. Class-based fee calculation
5. Student search using registration number
6. Marks entry for five subjects
7. Complete student information display
8. Fee details display
9. Input validation for important fields

## Registration Number

Each new student receives a unique registration number automatically.

```text
26ST0001
26ST0002
26ST0003
```

The number starts from `26ST0001` and increases by one for every new registration.

## Information Collected

### Personal Details

- Student name
- Mobile number
- E-mail ID
- Age
- Gender
- Class
- Registration number

### Parent's Details

- Father's name
- Mother's name
- Father's occupation
- Parent's mobile number

## Fee Structure

| Class | Admission Fee |
|------:|--------------:|
| 1 to 5 | Rs. 20,000 |
| 6 to 8 | Rs. 30,000 |
| 9 to 12 | Rs. 35,000 |

The fee is calculated automatically according to the class entered during registration.

## Subjects and Marks

Marks can be entered out of 100 for these five subjects:

- CHY
- PHY
- MAT
- CSE
- ENG

The program checks that every mark is between 0 and 100.

## Main Menu

```text
1. NEW REGISTRATION
2. SEARCH DETAILS
3. ASSIGN MARKS
4. INFORMATION FILE
5. FEES VIEW
6. EXIT
7. BACK
```

## Requirements

- Python 3
- No external libraries
- No database
- No file handling
- No web browser or internet connection

## Installation Instructions

### 1. Install Python

Download and install Python 3 from the official Python website. During installation on Windows, select the option **Add Python to PATH**.

Check the installation by opening Command Prompt or Terminal and entering:

```bash
python --version
```

If that command does not work, try:

```bash
python3 --version
```

### 2. Download the Project

Keep these files inside the same folder:

```text
admission_process.py
README.md
```

No additional package or library installation is required because the project uses only built-in Python features.

### 3. Open the Project Folder

Open Command Prompt or Terminal and move to the folder containing the project.

Example on Windows:

```bash
cd Desktop\Admission-Process
```

Example on macOS or Linux:

```bash
cd ~/Desktop/Admission-Process
```

### 4. Run the Program

On Windows, use:

```bash
python admission_process.py
```

On macOS or Linux, use:

```bash
python3 admission_process.py
```

The Admission Process menu will appear in the terminal. Enter a number from `1` to `7` to use a service.

### Running with Python IDLE

1. Open Python IDLE.
2. Select **File > Open**.
3. Open `admission_process.py`.
4. Select **Run > Run Module**, or press `F5`.

## How to Run

1. Save the Python code as `admission_process.py`.
2. Open it in IDLE or another Python interpreter.
3. Run the program.
4. Enter a serial number from the main menu.
5. Complete the requested details.

Example command:

```bash
python admission_process.py
```

## How to Use

### New Registration

Select option `1` and enter the student's personal details, class, and parent's details. The program will generate the registration number and calculate the fee.

### Search Details

Select option `2` and enter the registration number. The complete record of the student will be displayed.

### Assign Marks

Select option `3`, enter the student's registration number and class, and then enter marks for all five subjects.

### Information File

Select option `4` to search for one student or display every student registered during the current run.

> In this project, “Information File” is the name of a menu section. It does not create a physical file because file handling is not used.

### Fees View

Select option `5` to view the general fee structure. A student's fee can also be checked using the registration number.

### Exit

Select option `6` to close the program.

## Input Validation

The program performs the following checks:

- Mobile numbers must contain exactly 10 digits.
- The e-mail address must contain `@` and `.`.
- Age must be greater than zero.
- Class must be between 1 and 12.
- Registration number must exist before marks are entered.
- The entered class must match the registered class.
- Marks must be between 0 and 100.

## Data Storage

Student records are stored in the `students` dictionary. Each registration number is used as a unique dictionary key.

Example structure:

```python
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
```

## Important Limitation

Since file handling is not used, all records exist only while the program is running. The saved student details will be removed when the program is closed.

## Possible Future Improvements

- Add password protection for assigning marks
- Add permanent file or database storage
- Add fee payment status
- Add update and delete options
- Calculate total marks, percentage, and grade
- Improve e-mail validation

## Author

Developed as a Python console project for practising functions, loops, conditions, dictionaries, input validation, and exception handling.
