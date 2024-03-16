print("Day_5")

'''
print("Inheritence")
class Faculty:
    def __init__(self,f_name,dep,f_id):
        self.name=f_name
        self.dept=dep
        self.id=f_id
    def display(self):
        #print("Info::")
        print("Name:",self.name)
        print("Department:",self.dept)
        print("ID:",self.id)
obj1=Faculty("Siddiq","IT",100)
obj1.display()
class IT(Faculty):
    pass
obj=IT("Oppenhiemer","Nuclear Physiscs",101)
obj.display()'''
'''

## create a class of name placements which has a function info which displays the number of placements this year (623 selects and still counting**)
## create another class named department with function display which will display the names of departments present in the college
## create a class pragati withe the funciton welcome() which displays the messafe (Welcome to pragati college we are glad to have oyu onboard)
## pragati class should also display the details about departments and placements
class placements:
    #placements class--- grandparent
    def info(self):
        print("623 selects and still counting**")
class department(placements):
    #departments class--parent
    def display(self):
        self.list_1=["IT","CSE","CSE-DS","CSE-AIML","EE","CIVIL"]
        print("Departments:",str(self.list_1))
class pragati(department):
    #pragati class---child
    def welcome(self):
        print("Welcome to Pragati Engineering College\nWe are glad to have you on board")'''
        #'''obj2=department()
        #o#bj2.info()
        ########ob#j2.display()'''
        #'''
#start if the main program
'''
obj=pragati()
obj.welcome()
obj.info()
obj.display()

'''
''' multiple inheritence
class ferrari:
    def ferrari_WDC(self):
       return "Sebastian Vettel"
class mclaren:
    def mclaren_WDC(self):
        return "Lando Norris"
class mercedes_AMG(ferrari,mclaren):
    def mercedes_AMG_WDC(self):
        return "Lewis Hamilton"
wdc=mercedes_AMG()
print("The greatest F1 Drivers are: \nFerrari:",wdc.ferrari_WDC(),"\nMClaren:",wdc.mclaren_WDC(),"\nMercedes_AMG:",wdc.mercedes_AMG_WDC())
end of multiple inheritence'''


### polymorphism
##COMPILE TIME POLYMORPHISM----method overloading
'''
## THIS IS COMPILE TIME POLYMORPHISM
class Arithmatic:
    def mul(self,a):
        print(a)
    def mul(self,a,b):
        print(a*b)
    def mul(self,a,b,c):## PYTHON ONLY REMEMBERS THIS DEF FOR THE ADD FUNCTION 
        print(a*b*c)
obj=Arithmatic()
#obj.mul(5)
#obj.mul(12,12)
obj.mul(12,2,5)
## PYTHON DOESNT SUPPORT FUNCTION OVERLOADINGG
'''

#RUN TIME POLYMORPHSIM(EXE. TIME POLYMORPHISM)---->method overriding
'''
class Scuderia_Ferrari:
    def driver(self):
        print("I am Carlos Sainz, a Formula 1 driver")
    def team(self):
        print("I drive for scuderia Ferrari")
class carlos(Scuderia_Ferrari):
    pass
    #def team(self):
     #   print("I am currently unemployed!!!")
sainz=carlos()
sainz.driver()
sainz.team()
'''
#CONSTRUCTOR OVERRIFIDING
'''def Mercedes:
     def __init__(self):
         print("i Might join Mercedes")'''

#abstraction
# create a class ticketwjocj will be the abstract class
# inside that create an abstract function bookticket() and has nothing in it
#create a class makeMyTrip() which will use the book ticket function from ticket classto take the details such as
        ## name , phonenumber, emailid journey date nad displays a message saying thank oyu for booking from makeMyTrip
#create a class irctc which uses the bookticket() of ticket class and takes the same details as makemytrip but in the end it will give an option to the user to select wheather it is one way or round trip
    ## if the user option is reoundtrip it again asks the user to enter the return date as well and then prints a message "thank you for choosing irctc" else it prints the message "thank you for choosing irctc".
#create a class Indigo which states all the details as irctc and just asks which mode of transport you want to go in
    ## train flight or bus and displays thank you for choosing the Indigo

'''
#start of the program
from abc import ABC,abstractmethod
#abstract class
class ticket:
    @abstractmethod
    def bookticket(self):
        pass
##endof abstract class

#start of makemytrip class
class makeMyTrip(ticket):
    def bookticket(self):
        name=input("Enter the name:")
        num=int(input("Enter the phonen number:"))
        email=input("Enter the email_ID:")
        jr_dt=input("Enter the date in DD-MM-YYYY format:")
        print("Thank you for booking from makeMyTrip")
## end of makemytrip class

#start of IRCTC class
class irctc(ticket):
    def bookticket(self):
        name=input("Enter the name:")
        num=int(input("Enter the phonen number:"))
        email=input("Enter the email_ID")
        jr_dt=input("Enter the jpurney date in DD-MM-YYYY format:")
        flag=1
        while flag==1:
            print("Wanna do the roundtrip??: \n1.Yes \n2.No")
            rd_trip=input()
            if rd_trip=="yes" or rd_trip=="1":
                rt_dt=input("Enter the  return date in DD-MM-YYYY format:")
                print("Thank you for booking from irctc")
                flag=0
            elif rd_trip=="no" or red_trip=="2":
                print("Thank you for booking from irctc")
                flag=0
            else:
                print("Invalid Response!!! please try again")
            
        
## end of IRCTC class

##start of Indigo class
class Indigo(ticket):
    def bookticket(self):
        name=input("Enter the name:")
        num=int(input("Enter the phonen number:"))
        email=input("Enter the email_ID")
        jr_dt=input("Enter the date in DD-MM-YYYY format:")
        print("Thank you for booking from INDIGO")
## end of INDIG class
##Start of the main program
flag=0
while flag==0:
    print("Enter Your  Mode Of Transportation \n1.Flight\n2.Train\n3.Bus")
    mode=input()
    if mode=="1" or mode=="Flight":
        obj=Indigo()
        obj.bookticket()
        flag=1
    elif mode=="2" or mode=="Train":
        obj=irctc()
        obj.bookticket()
        flag=1
    elif mode=="3" or mode=="Bus":
        obj=makeMyTrip()
        obj.bookticket()
        flag=1
    else:
        print("Invalid Response!!!")

'''
#ENCAPSULATION

##create an atm system0 is the main task
    ## task-1 ::  Display the remaining amount in the ATM
    ## task-2 ::  Authentication of the user with username and password
                    # Rupay
                        #visa
                        #mastercard
            #:: if the iser is authenticated then giv him the following options to choose
            #1. Check Balance
            #2. Cash Withdrawl ---> post withdrawl bal to be displayed check for the limit of the atm bal tooo
                    # based on card transaction limit is there rupay-2k visa-5k mastercard-8499
            #3. Cash Deposit----> post deposit bal to be displayed
            #4. Mini statement of the last three Transactions
            #5. 
    ##Modules to be created
            #atm_crt
            #AUTHENTICATION
            #DISPLAY

    
