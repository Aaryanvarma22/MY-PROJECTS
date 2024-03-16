print("DAY 3 OF CRT ")
#  1.Write a function which takes two parameters a and b typecast the valuw of secomnd argument into int then multiply both the arguments and [rint the last digit of the result
'''def func(a,b):
    b=int(b)
    prod=a*b
    #print(prod)
    digit=prod%10
    print(digit)
n1=int(input("a:"))
n2=float(input("b:"))
func(n1,n2)'''

''' 1.for default argument 
def npta(name,place="banglore"):
    print(name," from ",place)
    print("Awesome bruv")
    
name=input("Name:")
npta(name)'''


''' 2.for the positional arguments
def det(name,age):
    print("I am ",name,"and I am",age)

name=input("Enter a Name:")
age=int(input("Enter the Age:"))
det(age=age,name=name) '''

''' 3. for the 
def func(a,b):
    b=int(b)
    prod=a*b
    #print(prod)
    digit=prod%10
    print(digit)
n1=int(input("a:"))
n2=float(input("b:"))
func(n1,n2)'''

# 2. Write a functionm to calculate the sum of first and last digit of a number
'''def sumfl(n):
    count=0
    while(n>0):
        digit=n%10
        count+=1
        n=n//10
        if count==1:
            last_digit=digit
    print(digit+last_digit)
n=int(input("Enter your number"))
sumfl(n)'''

################''' better alternative'''
'''def check(n):
    sum=n%10
    while n>=10:
        n=n//10
    sum+=n
    print("Sum:",sum)

n=int(input("Enter The Number:"))
check(n)'''##########################

# 3.write a log in function which accepts the user only when the username and password are same and displays a mesng log in successfull otherwise it keeps asking the user to enter the credentials untill they are correct  

'''def login():
    us_nm=input("Enter UserName:")
    pas=input("Enter Password:")
    username="Siddiq"
    password="IamBatman@61"
    if us_nm==username and pas==password:
         return True         
    else:
        print("Log in Failed ")
        return False
    
while True:
    if(login()==True):
        print("Login Successfull!")
        break
print("out of Loop")

 ### A better solution would be to include the while loop in the login function itself that makes us to call the funciton just once else the function is called upon multiple times'''

# 4. Fibb using recursion
'''def fibbs(n):
    while(n>0):
        if n==1:
            return 0
        elif n==2:
             return 1
        else:
            return fibbs(n-1)+fibbs(n-2)
n=int(input("Enter the number: "))
print("The Sum is : ",fibbs(n))'''

# 5.Factorial using recursion
'''def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
n=int(input("Enter the number:"))
print("FActorial ",fact(n))'''


# 6.Write a recursive program to print a number in revese order
## here the the idea for recursive logic which number should be recursify
'''
def rev(n):
    if(n!=0):
        print(n%10,end="")
        rev(n//10)
n=int(input("Enter the number:"))
rev(n)'''
#7. wriite a recursive function to count the number of digits of a number
'''
def rev(n): 
    if(n==0):
        #print(n%10,end="")
        return 0
    else:
        return 1+rev(n//10)#returning the count itself

n=int(input("Enter the number:"))
print("the number of digits are:",rev(n))
'''

# 8. write a recursive functuion to calculate the sum of digits of anumber
'''
def sums(n):
    if(n!=0):
        dig=n%10
        return dig+sums(n//10) # returning the sum itself
    else:
        return 0
n=int(input("Enter the number:"))
print("the number of digits are:",sums(n))'''

# 9. write the recursive function to find the armstrong
'''def count(n): 
    if(n==0):
        #print(n%10,end="")
        return 0
    else:
        return 1+count(n//10)
def arms(n,c):
    if(n>0):
        dig=n%10
        return dig**c+arms(n//10,c)
    else:
        return 0
       
n=int(input("Enter your number:"))
c=count(n)
res=arms(n,c)
if(res==n):
    print("Great Work Armstrongggg!!!!!!!!!")
else:
    print(res,"Not Armstring Bruvvv")'''
# 10. write a recursive function to check if the number is palindrome
''''def pals(n):
    if n>0:
        dig=n%10
        return dig+(pals(n//10)*10)
    else:
        return 0
n=int(input("Enter the number Bruvv:"))
res=pals(n)
if(res==n):
    print("Palindrome dudeeee")
else:
    print("Not a palindrome Bruvvv")'''

# 11.create access append slice insert update a list
'''
list_1=["Batman","Arkham",1,44]#creating a list
print()
print(list_1[0],"is the knight of",list_1[1])#accessing the list
print()
#print(list_1[1:4])#slicing
print(list_1[1:5:2])#slicing
print()
list_1.append("Gotham")#appending
print(list_1)
print()
list_1[1]="Arkham_Asylum"#mutability
print(list_1[1])
print()
list_1.insert(1,True)#inserting into the list
print(list_1)
print()
for i in range(0,len(list_1)):#loop accessing
    print(list_1[i],end=" Version 0")
    print()
for i in list_1:
    print(i,end=" ")
   
mylist=[["Batman",True],[44,"Legend"],["Max",1]]
for i in range(0,len(mylist)):
    print(mylist[0],"IS",mylist[1])
     '''
# 11.
'''
list_pr=[12,42,96,7,18,10,133]
#add of min and max
mins=list_pr[0]
maxs=0
for i in list_pr:
    if(i>maxs):
        maxs=i
    if(i<mins):
        mins=i
print("minimum is:",mins)
print("maximum is:",maxs)
sums=maxs+mins
diff=abs(mins-maxs)
print("Sum is:",sums)
print("diff is:",diff)
for i in range(len(list_pr)):
    if(list_pr[i]==mins):
        list_pr[i]=diff
        #print("New Min is:",i)
    if(list_pr[i]==maxs):
       list_pr[i]=sums
       #print("New Max is:",i,"at",i)

print("Updates list:",list_pr)
print()
## this can be done in a single loop
'''

# 12. creating of tuples adding values manually into atuple data accessing
'''
tups=("Siddiq",61,True)#creation of a tuple
print(tups)
print(tups[1])#accessing
tupss=tups+(5,"Batman","Siddiq",)#Instertng an element manually
print(tupss)
print()
for i in range(0,2):#looping
    n=int(input("Enter"))
    tups=tups+(n,)
print(tups)'''

# 13. create your dictionary with atleast four key value pairs++
    #accessing your values using keys++
    #accessing the whole dict using for loops++
    #check adding duplicate values and keys
    #check for mutability in dict ++
    #remove a key value pair from dict
dicts={101:"Batman",102:"is",103:44,104:"lewisssss"}#created a dictionary
print(dicts)
print(dicts[104])#accessing
dicts[104]="Max"
print(dicts)#mutability!!
for i in dicts:#accessing the whole dict
    print(dicts[i])











    







    


    
