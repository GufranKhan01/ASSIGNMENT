students_marks={
    "Alice":90,
    "Faizan":45,
    "Irfan":70
}

students_name=input("Enter the student's name:")
if students_name in students_marks:
     print(f"{students_name}'s marks: {students_marks[students_name]}")

else:
     print(f"student not found.")
