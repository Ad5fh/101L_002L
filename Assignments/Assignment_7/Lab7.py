## Aissatou Diallo
## ad5fh@umsystem.edu 
## CS 101 Lab
##PROBLEM: Weighted Grades
##Algorithm: The program below is calculating the grade weight of a student by using  his/her scores. The table contains the average grade of the student, the minimum and the maximum score, the standard deviation and the average.  
#################################################################################################################################

import math   
def get_std(grade,avg):
    count=len(grade)
    sum=0
    for grades in grade:
        sum = sum + (grades-avg)**2  
    std=math.sqrt(sum/count)
    return std
    
def get_avg(grade):
    count=len(grade)
    if grade ==0:
        return 0
    else:
        sum=0
        for i in grade:
          sum+=i
        return (sum/count)
def get_table(grade,text):
    weighted_scores=0.00
    print("Type\t\t\t#\t\t min\t\t max\t\t avg\t std")
    print("="*84)
    if len(grade)==0:
        avg="n/a"
        std="n/a"
        minimum= "n/a"
        maximum="n/a"
        print("Tests","\t\t\t",len(grade),"\t\t",minimum,"\t\t",maximum,"\t\t",avg,"\t",std)
        
    elif len(grade) > 0:
        avg1=get_avg(grade)
        std=get_std(grade, avg1)
        minimum=min(grade)
        maximum=max(grade)
        weighted_scores+=avg1 * 0.6
        print("Tests","\t\t\t",len(grade),"\t\t",minimum,"\t\t",maximum,"\t\t","{:.2f}".format(avg1),"\t","{:.2f}".format(std))
    if len(text)==0:
        avg="n/a"
        std="n/a"
        minimum= "n/a"
        maximum="n/a"
        print("Programs","\t\t",len(text),"\t\t",minimum,"\t\t",maximum,"\t\t",avg,"\t",std)
        
    elif len(text) > 0:
        avg1=get_avg(text)
        std=get_std(text, avg1)
        minimum=min(text)
        maximum=max(text)
        weighted_scores+=std * 0.4
        print("Programs","\t\t",len(text),"\t\t",minimum,"\t\t",maximum,"\t\t","{:.2f}".format(avg1),"\t","{:.2f}".format(std))
    print("The weighted scores is     ","{:.2f}".format(weighted_scores))
    

test=[]
assignment=[]

that=True
while that:
 print("\t\tGrade Menu")
 print("1 - Add Test")
 print("2 - Remove Test")
 print("3 - Clear Tests")
 print("4 - Add Assignment")
 print("5 - Remove Assignment")
 print("6 - Clear Assignments")
 print("D - Display Scores")
 print("Q - Quit")
 print()
 selection=input("==> ")

 if selection=='1':
     while True:
         score1=float(input("Enter the new test score 0-100 ==> "))
         if 0 < score1 <= 100:
             test.append(score1)
             break
 elif selection=='2':
     score1=float(input("Enter the Test to remove 0-100 ==> "))
     try:
       test.remove(score1)
     except ValueError:
       print("Could not find that score to remove")
     test.remove(score1)
 elif selection=='3':
      test.clear()
 elif selection=='4':
     score2=float(input("Enter the new Assignment score 0-100 ==> "))
     assignment.append(score2)
 elif selection=='5':
   score2=float(input("Enter the Assignment to remove 0-100 ==> "))
   try:
     assignment.remove(score2)
   except ValueError:
     print("Could not find that score to remove")

 elif selection=='6':
     assignment.clear()
 elif selection=='D'or selection=='d':
     get_table(test,assignment)
 elif selection=='q' or selection=='Q':
     break