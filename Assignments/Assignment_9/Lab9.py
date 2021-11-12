## Aissatou Diallo
## ad5fh@umsystem.edu 
## CS 101 Lab
##PROBLEM: Word Count
##Algorithm: The program below read a txt file and output the specific information we need from the file. In this case we want to count the number of words we have in the file and the frequence at which they appeared in the file.
#################################################################################################################################



def readfile(filename):
    file= open(filename,encoding='utf-8')
    diction1={}
    reader=file.read().split()
    print()
    print("Most frequently used words")
    print("#            Word                    Freq.")
    print("==========================================")
    count=0
    for data in reader:
        data=data.strip('!.,-*&^%$#@!+=";:/?><|\()][}{')
        data=data.lower()
        words=data.split(" ")
        for word in words:
            if word in diction1:
                diction1[word]+=1
            elif len(word) > 3:
                diction1[word]=1
            
    for key in list(diction1.keys()):
        if len(key)>3:
            count+=1
            print('{:<5}{:>12}{:>25}'.format(count,key,diction1[key])) 
    unique=0
    appeared_once=0
    for values in diction1.values():
        if values == 1:
            unique +=1
            appeared_once += 1
        else:
            appeared_once+=1       
    print("There are",unique,"words that occur only once")
    print("There are",appeared_once,"unique words in the document")
                  
while (1):
    try:
        user_input=input("Enter the name of the file to open ")
        content=readfile(user_input)
        break
    except FileNotFoundError:
        print("Could not open file "+user_input)
        print("Please Try again")
        print()
        continue

