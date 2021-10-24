## Aissatou Diallo
## ad5fh@umsystem.edu 
## CS 101 Lab
##PROBLEM: Fuel Economy
##Algorithm: The program below is to read the data of the Fuel Economy file by using File Handling, Try Except method and 3 functions.The main thing in this lab was to open the file read it and convert some of the data of the original file to a new file. 
#################################################################################################################################

#Accessing the right data in the main file
def get_mpg():
    while True:
        try:
            minimum_mpg=float(input("Enter the minimum mpg ==> "))
            if minimum_mpg<0:
                print("Fuel economy given must be greater than 0")
            elif minimum_mpg>100:
                print("Fuel economy given must be less than 100")
            else:
                return minimum_mpg
        except:
            print("You must enter a number for the fuel economy")
#opening the main file and read it
def get_file():
    while True:
        filename=input("\nEnter the name of the input vehicle file ==> ")
        try:
            with open(filename,'r') as readfile:
                return [[data.strip() for data in line.strip().split('\t')] for line in readfile.readlines()]        
        except:
            print("Could not open file",filename)
#converting some data from the main file to a new file
def get_newfile(minimum_mileage,filedata):
    while True:
        try:
            filename=input("Enter the name of the file to output to ==> ")
            with open(filename,'w') as writefile:
                for content in filedata:
                    try:
                        if minimum_mileage>=float(content[7]):
                            writefile.write('{0:<5}{1:<40}{2:<40}{3:>10}\n'.format(content[0],content[1],content[2],content[7]))
                    except:
                        print("Could not convert value", "{}".format(content[7]), "for vehicle", "{} {} {}".format(content[0],content[1],content[2]))
        except :
            print("There is an IO Error", filename)
            

def main():
        minimum_mileage=get_mpg()
        filedata=get_file()[1:]
        print()
        get_newfile(minimum_mileage,filedata)
      
main()

             