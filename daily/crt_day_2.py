print("          PATTERNS         ")
#1). To print the left sided upward trianle
'''
for i in range(1,6):
   for i in range(1,i+1):
        print("@*",end="")
    print()
'''


#2). To print the pattern in a downward triangle
'''
#for i in range(1,5):
##   for j in range(1,i+1):
#      print(i,end="")
#   print()
   
#for i in range(5,0,-1):
#    for j in range(i,0,-1):
#      print(i,end="")
 #   print()
##
'''

#       }



#3). To print the pattern with space first
'''
for i in range(1,5):
    #spaces
    for s in range(1,5-i):
        print(" ",end="")
    #for *
   for j in range(1,i+1):
        print("*",end="")
    print()
    '''



##4). To print border pattern
'''
r=int(input("Enter number of rows:"))
for i in range(1,r+1):
    for j in range(1,r+1):
        if(i==1 or i==r or j==1 or j==r):
            print("@",end=" ")
        else:
           print(" ",end=" ")
    print()
'''

## 5). To print Floyyds triangle#
'''
count=0
for i in range(1,6):
   for j in range(1,i+1):
       count+=1
       print(count,end=" ")
    print()
'''

## 6) To print the arrow o
'''
for i in range(1,10):
#for j in range(
'''

## 7). to print a pyramid of starts
'''
r=int(input("Enter number of rows"))
for i in range(0,r+1):
    for s in range(1,r-i+1):
       print(" ",end=" ")
   for j in range(1,2*i):
        print("*",end=" ")
    print()
'''
##8). To print a hollow pyramid

          
        



