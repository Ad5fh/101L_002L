########################################################################
##
## CS 101 Lab
## Program #:The Great and Powerful Flarsheim (Flarsheim Guesser)
## Name: Aissatou Diallo
## Email:Ad5fh@umsystem.edu
##
## PROBLEM : The code below help us output the number we think in our head after we put the right reminders for 3, 5 and 7.
##
## ALGORITHM : see below
########################################################################
#For this assignment, the indentation is very important because if they are not done correctly, the loop won't work correctly.

print("Welcome to the Flarsheim Guesser!")
print()
while True:
    print("Please think of a number between and including 1 and 100.\n")
    remainders="357"
    print()
    list_remainders = []
    for i in remainders:
        while True:
            print("What is the remainder when your number is divided by ",i,"? ",end="")
            remainder = int(input())
            if remainder<0:
                print("The value entered must be 0 or greater")
                continue
            elif (remainder>=int(i)):
                print("The value entered must be less than ",i)
                continue
            else:
                if(i!='7'):
                    print()
                list_remainders.append(remainder)
                break
    for j in range(1,101):
        if j%3==list_remainders[0] and j%5==list_remainders[1] and j%7==list_remainders[2]:
            print("Your number was",str(j))
            print("How amazing is that?\n")
            break

    guess=' '
    while True:
        print("Do you want to play again? Y to continue, N to quit ==> ",end="")
        guess=input()
        if (guess=='n'or guess=='N'or guess=='y'or guess=='Y'):
            break
        else:
            continue

    if(guess=='n' or guess=='N'):
        break
    elif(guess=='y' or guess=='Y'):
        print()
