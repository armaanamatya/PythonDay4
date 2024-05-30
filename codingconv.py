# Create a Python program that manages student records. The program should have the
# following functionalities:
# - Create a function that can add new students to the records with their student_id, name, age, and grade. 
# The records should be saved to “json” file and each time
# new record is added, it should be saved to same “json” file
# - Allow searching for a student by student_id or name. The data should return age and grade from the saved file.
# - Allow updating a student's information by using student_id or name(age or grade)

import json
import os

# Define the path to the JSON file
FILE_PATH = 'student_records.json'


def load_records():
    """
    Load the student records from the JSON file.
    Returns
        A list of student records.
    """
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r', encoding='utf-8') as file:
            return json.load(file)
    return []


def save_records(records):
    """
    Save the student records to the JSON file.
    Parameters
    ----------
    records : list
        A list of student records to save.
    """
    with open(FILE_PATH, 'w', encoding='utf-8') as file:
        json.dump(records, file, indent=4)


def add_student(student_id, name, age, grade):
    """
    Add a new student to the records.

    Parameters
    ----------
    student_id : int
        The ID of the student.
    name : str
        The name of the student.
    age : int
        The age of the student.
    grade : str
        The grade of the student.
    """
    records = load_records()
    records.append({
        'student_id': student_id,
        'name': name,
        'age': age,
        'grade': grade
    })
    save_records(records)


def find_student_by_id(student_id):
    """
    Find a student by their student ID.

    Parameters
    ----------
    student_id : int
        The ID of the student to find.
    Returns
    -------
    dict or None
        The student's record if found, otherwise None.
    """
    records = load_records()
    for student in records:
        if student['student_id'] == student_id:
            return student
    return None


def find_student_by_name(name):
    """
    Find a student by their name.

    Parameters
    ----------
    name : str
        The name of the student to find.

    Returns
    -------
    dict or None
        The student's record if found, otherwise None.
    """
    records = load_records()
    for student in records:
        if student['name'] == name:
            return student
    return None


def update_student(student_id=None, name=None, age=None, grade=None):
    """
    Update a student's information.
    Parameters
    ----------
    student_id : int, optional
        The ID of the student to update (default is None).
    name : str, optional
        The name of the student to update (default is None).
    age : int, optional
        The new age of the student (default is None).
    grade : str, optional
        The new grade of the student (default is None).
    """
    records = load_records()
    for student in records:
        if student['student_id'] == student_id or student['name'] == name:
            if age is not None:
                student['age'] = age
            if grade is not None:
                student['grade'] = grade
            save_records(records)
            return
    print("Student not found.")


add_student(1, 'Armaan', 20, 'A')
add_student(2, 'Bob', 21, 'B')

# Search for students
student = find_student_by_id(1)
print(student)

student = find_student_by_name('Bob')
print(student) 

# Update a student's information
update_student(student_id=1, age=21, grade='A+')
print(find_student_by_id(1))