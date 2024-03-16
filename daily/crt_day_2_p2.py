#1).To print the given number in reverse find the sum prod and number of digits


'''num=int(input("Give a number"))
sum=0
rem=num%10
count=1
prod=1
print("reverse order:",end=" ")
while num!=0:
    rem=num%10
   print(int(rem),end=" ")
   sum+=rem
    prod*=rem    
    num=num-rem
    num=num/10
    count+=1
#while num>0:
#    digit=num%10
#    print(digit,end=" ")
#    sum+=digit
#    prod*=digit
#    count+=1
#    num=num//10
print()
print("total:",count-1)
print("Sum:",int(sum))
print("Product:",int(prod))'''



#2). Take an int from the user and check weather if the number is divisible by sum of digits or no
'''
n=int(input("Gimme your num bruv:"))
s=0
num=n
while num>0:
   digit=num%10
    s+=digit
   num=num//10
print("Sum of the digits for the number is ",s)
if n%s==0:
    print("Awesome bruv, your number is divisible")
else:
   print("Try again bruvv!!")'''




#3).take a number ionput from the user check if the sum of factors of that number is greater than the orignal number or not if yes else no
'''
n=int(input("Gimme the number jeff:"))
num=n
sum=0
divs=1
while divs<=n/2:
    if n%divs==0:
        sum+=divs
   divs+=1
if sum>n:
   print(sum,"Godly Bruv")
else:
   print(sum,"come on bruvvvvv!")'''


 
##4). Calculate the diff of sum of numebrs that are divisble by six and not divisible by six in the range of first 30 number
'''
sum1=0
sum2=0
num=1
while num<=30:
   if num%6==0:
       sum1+=num
    else:
       sum2+=num
   num+=1
print(abs(sum1-sum2))
'''
 
  ##5)plaindrome number
'''
n=int(input("Give me your number bruv"))
rev=0
og_num=n
while n>0:
   rem=n%10
    rev=(rev*10)+rem
    print(rev)
    n=n-rem
    n=n//10  
if(og_num==rev):
    print(rev,"Its Palindrome you are on a Roll bruv!!")
else:
    print(rev,"Not a Palindrome Bruv")
'''



##  6).ArmStrong number
'''
n=int(input("Hit me with your number man:"))
og_num=n
count=0
arms=0
while n>0:
    rem=n%10
    count+=1
    n=n-rem
    n=n//10
   print(n)
n=og_num
while n>0:
    dig=n%10
    arms+=(dig)**count
    n=n-dig
    n=n//10
if arms==og_num:
    print(arms,"good Work ARMSYYY")
else:
    print(arms,"Not ARMSYYY")
'''
##  7)add the digits with thier position 
'''
n=int(input("Hit me with your number man:"))
og_num=n
count=0
arms=0
while n>0:
    count+=1
    n=n//10
print(count)
n=og_num
while n>0:
    rem=n%10
    arms+=(rem)**(count)
    n=n-rem
    n=n//10
    count-=1
'''
#print("The sum of the digits swuared to their positions is :", arms)

##  8)
#
#

    
    

    
