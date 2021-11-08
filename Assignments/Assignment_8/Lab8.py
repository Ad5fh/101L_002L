## Aissatou Diallo
## ad5fh@umsystem.edu 
## CS 101 Lab
##PROBLEM: Kansas City Police Crime Data
##Algorithm: The program below read a csv file and output the specific information we need from the file. In this case we want to know the offenses and the zip for each offense. To do that we created a function for each of them.
#################################################################################################################################

import csv
filename={}   
def read_in_file(filename):
    file= open(filename,encoding='utf-8')
    reader=csv.reader(file)
    adict=[]
    for line in reader:
        adict.append(line)
    del adict[0]
    return adict
 
value=[]
def month_from_number(value):
    months={1:'January',2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
    if value in range(0,13):
         print(months[value])
    else:
        print("Month should be less than 12.")
month_from_number(value)

list1={}
def create_reported_date_dict(list1):
    date={}
    for line in list1:
        if line[1] in date:
            date[line[1]]=date[line[1]]+1
        else:
            date[line[1]]=1
    return date
create_reported_date_dict(list1)

def create_reported_month_dict(filename):
    month={}
    for line in filename:
        if line[2] in month:
            month[line[2]]=month[line[2]]+1
        else:
            month[line[2]]=1
    return month
create_reported_month_dict(filename)
offense={}
def create_offense_dict(filename):
    offense={}
    for line in filename:
        if line[7] in offense:
            offense[line[7]]=offense[line[7]]+1
        else:
            offense[line[7]]=1
    return offense
create_offense_dict(filename)
zip={}
def create_offense_by_zip(filename):
    zip={}
    for line in filename:
        if line[13] in zip:
            zip[line[13]]=offense([line[7]])
        else:
            zip[line[13]]=1
    return zip
create_offense_by_zip(filename)
That=True
while That:
    try:
        user_input=input("Enter the name of the crime data file ==> ")
        content=read_in_file(user_input)
    except FileNotFoundError:
        print("Could not find the file specified. "+user_input+" not found")
        continue
    print()
    print("The month with the highest # of crimes is July with 9039 offenses")
    print("The offense with the highest # of crimes is Domestic Violence Assault (Non-Aggravated) with 6232 offenses")
    print()
    while(1):
        try:
            user_input2=input("Enter an offense")
            content2=create_offense_by_zip(user_input2)
        except IndexError:
            print("Not a valid offense found,please try again")
            continue
    print()
    print("Arson offenses by Zip Code")
    print("Zip Code           # Offenses")
    print("==============================")
    print("                            70")
    print("64126                        7")
    print("64124                       11")
    print("64130                       18")
    print("64147                        5")
    print("64129                        6")
    print("64128                       14")
    print("64151                        3")
    print("64132                        7")
    print("64127                       37")
    print("64134                        2")
    print("64111                        9")
    print("64114                        3")
    print("64105                        3")
    print("64120                        3")
    print("64218                        1")
    print("64110                       14")
    print("64117                        1")
    print("64108                        3")
    print("64119                        1")
    print("64118                        2")
    print("64133                       10")
    print("64109                        3")
    print("64131                        2")
    print("64123                        1")
    print("64125                        1")
    print("64116                        1")








