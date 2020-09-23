exam = int(input("Input exam score:"))
attendance = int(input("Input attendance:"))
if attendance <= 90:
    grade = "Fail"
else:
    if exam > 90:
        grade = "A"
    elif exam > 80:
        grade = "B"
    elif exam > 70:
        grade = "C"
    else:
        grade = "Fail"
    #end if
#end if

print("Grade:",grade)
