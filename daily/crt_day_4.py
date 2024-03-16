print("DAY 4")
'''# 1.list=[-1,42,65,1,-4,6] write a program to find the second smallest negative number fro the list without using srot min or

listt=[22,45,65,1,-4,6,-1]
listt=[]'''
'''
n=int(input("Enter the size of youe list:"))
for i in range(0,n):
    elm=int(input())
    listt.append(elm)'''
''''
mins=listt[0]
mins2=0
flag=0
count=0
for i in listt:
    if i<mins:
        if i<0:
            mins2=mins
            flag=1
            count+=1
        mins=i
        if mins2>i and mins2>mins:
            mins2=i
        
if flag==0:
    print("no negative number man")
else:
    print("Your second smallest minimum is:",mins2)'''

# 2.set
'''aaryan_set={61,"siddiq",63.5,True}
print(aaryan_set[1])'''

#3.listtt=[2,0,1024,0,40,230,0] shift all the 0s to the right while maintaning the order
'''list1=[2,0,1024,0,40,230,0]
list2=[]
count=0
for i in range(0,len(list1)):
    if list1[i]==0:
        count+=1
        list2[count]=list1[i]
for i in range(0,len(list1)-count):
    if(list1[i]!=0):
        list2[count]=list1[i]
print(list2)'''

# 4. create a class f_15 with functions lights fans and AC
    #lights-- when it is called it prints out the color of the light which is taken as parameter to the function
    #fans---- when it is called it displays the speed of the regulator , ehich is taken as the parameter for the function
    #AC------ diplays the room temperature and the outside temp which are taken as parameters
    #write a fourth function hwose nakme is display which displays the diff in outside and room temp from ac and also the fan speed
'''
class f_15:
    def __init__(siddiq,a,b):
        siddiq.start=a
        siddiq.end=b
        print("Start Time:",siddiq.start)
        print("end Time:",siddiq.start)
    def lights(siddiq, color):
        print("the color of the loght is:",color)
    def fans(siddiq, speed):
        siddiq.sped=speed
        print("the speed of the fan is:",siddiq.sped)
    def ac(siddiq, r_temp,o_temp):
        siddiq.diff= abs(r_temp-o_temp)
        print("the put and in temp :",r_temp," and ",o_temp)
    def display(siddiq):
                print("the diff in temps is:",siddiq.diff)
                print("the speed of the fan is:",siddiq.sped)
                print("Start Time:",siddiq.start,"End Time:",siddiq.end)
                
## end of class
obs=f_15(9.00,4.20)
obs.lights("red")
obs.fans(5)
obs.ac(17,34)
obs.display()
'''

## PROJECT CAR SHOWROOM
    #WHEN they select the brand and model the details of milage and onroad price should be displayed
    #only three car companies toyota mahindra and mercedes
   # '''done'''# #take the input from the user for the car company name and in the input message five the user the option of three coma0pnies
    #this user input company name goes as the input/argument to the model_name function,which welcomes the user accordingly to the company name
    #'''done'''# #then ask the user to enter the specific model namefor that company fro the optio sgiven
    #'''done'''# #the second function whose name is variant. According to the car company name and car model the user shpould be asked to enter the variant  he would like to choose Petrol Diesel and hybrid
        #The last Display function according to the car company, car modlename and car variaant first its EX_showroom price should be displayed and then its onroad price should be displayed #, which is calculated as
            ##PRICE=Ex_showroomprice+CGST+SGST+INSURANCE.
            ##the sgst cgst and insurance all the three have a comman value throught our the car showroom
   #################SHOULD BE ABLE TO
 #### mtry usnig sub classes toooooo


class car_showroom:
       ### start of the model_name function
    def model_name(self,car_comp):
        self.comps=car_comp
        print("HEY THERE!!!!!!!\nWelcome to the ",self.comps,"Family:)")
        if self.comps=="Mercedes" or self.comps=="1":
            print("1.G-Wagon \n2.Mayback \3.AMG A45")
            self.usermodel=input();                                                                                    
        elif self.comps=="Porsche" or self.comps=="2":
            print("1.Cayenne \n2.Panamera \3.911 Turbo")
            self.usermodel=input();
        elif self.comps=="Ferrari" or self.comps=="3":
            print("1.Portofino \n2.Tributo \n3.Purosangue")
            self.usermodel=input();
        else:
            print("Please Enter a Valid name")
            model_name(car_comp)

        ### end for the model name function
            
        ### start of the variant function
    def variant(self):
        print("Enter the variant you want to choose:\n1.Petrol \n2.Diesel")
        self.var=input();
        if self.var!="Petrol" and self.var!="Diesel" and self.var!="1" and self.var!="2":
            print("Invalid Variant");
            variant();
        ###End of the variant function

    def display(self):
        ## outer ifs are for checking the company name
        ## inner ifs are for checking the modelname

        #body for mercedes
        if self.comps=="Mercedes":
            if self.usermodel=="G-Wagon" or self.usermodel=="1":
                #body for G-wagon
                self.x_sh_pr=1800000
                cgst=(8/100)*x_sh_pr
                sgst=(8/100)*x_sh_pr
                ins=90000
                print("EX-Showroom Price of",self.usermodel,"is:",self.x_sh_pr)
                price=x_sh_pr+cgst+sgst
                print("It costs you",price,"Come on Bruvv lets get this doneeeeee")
                
             elif self.usermodel=="Mayback" or self.usermodel=="2":
                #body for mayback
                
             elif self.usermodel=="AMG A45" or self.usermodel=="3":
                #body for AMG A45

        #body for porsche        
        elif self.comps=="Porsche":
            if self.usermodel=="Cayenne":
                #body for G-wagon
            elif self.usermodel=="Panamera":
                #body for mayback
            elif self.usermodel=="911 Turbo":
                #body for AMG A45

        #body for ferrari        
        elif self.comps=="Ferrari":
            if self.usermodel=="Portofino":
                #body for G-wagon
            elif self.usermodel=="Tributo":
                #body for mayback
            elif self.usermodel=="Purosangue":
                #body for AMG A45
        
        
        
    
    ## contents of the class
#### end of the class
    ##start of the main program
print("Choose your car company from the following:")
print("1.Mercedes \n2.Porsche \n3.Ferrari")
car_comp=input()## Taken the input from the user
cars=car_showroom()
cars.model_name(car_comp)
cars.variant()

    
