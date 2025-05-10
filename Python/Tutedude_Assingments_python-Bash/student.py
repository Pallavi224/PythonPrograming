
'''
2 Student Grades
Create a dictionary where the keys are student names and the values are their grades. Allow the user to:
Add a new student and grade.
Update an existing student’s grade.
Print all student grades.
'''

Student_Grades={"name1":"grade1","name2":"grade2","name3":"grade3"}
print("Student Grades Dictionary:",Student_Grades)
Student_Grades["name4"]="grade4" # Add a new student and grade
Student_Grades.update({"name3":"grade"})
print("Updated Student Grades Dictionary:",Student_Grades)
print("All Student Grades:",Student_Grades)
