print("**** Welcome to the LAB grade calculator! ****")
print()
name=input("Who are we calculating grades for? ==> ")
print()
lab_grade= int(input("Enter the Labs grade? ==> "))
if lab_grade<0:
  lab_grade=0
  print("The lab value should have been zero or greater. It has been changed to zero")
if lab_grade>100:
  lab_grade=100
  print("The lab value should have been 100 or less. It has been changed to 100.")
print()
exam_grade=int(input("Enter the EXAMS grade? ==> "))
if exam_grade<0:
  exam_grade=0
  print("The exam value should have been zero or greater. It has been changed to zero")
if exam_grade>100:
  exam_grade=100 
  print("The exam value should have been 100 or less. It has been changed to 100.")
print()
attendance_grade= int(input("Enter the Attendance grade? ==> "))
if attendance_grade<0:
  attendance_grade=0
  print("The attendance value should have been zero or greater. It has been changed to zero")
if attendance_grade>100:
  attendance_grade=100
  print("The attendance value should have been 100 or less. It has been changed to 100.")
print()
calculation= (lab_grade*0.7)+(exam_grade*0.2)+(attendance_grade*0.1)
print("The weighted grade for",name, "is", calculation)
if calculation >90 and calculation<=100:
    print(name,"has a letter grade of A")
elif calculation>80 and calculation<=90:
    print(name,"has a letter grade of B")
elif calculation>70 and calculation<=80:
    print(name,"has a letter grade of c")
elif calculation>60 and calculation<=70:
    print(name,"has a letter grade of D")
elif calculation>0 and calculation<=60:
    print(name,"has a letter grade of F")
print()
print("**** Thanks for using the Lab grade calculator ****")