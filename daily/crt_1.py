#a=int(input("a:"))
#if a%3==0 and a%6==0:
 #   print("Good number")
#elif a%2==0 and a%7==0:
 #   print("Average number")
#elif a%4==0 and a%9==0:
 #   print("Awesome number")
#else:
 #   print("Bad Number")

for i in range(0,2000):
    if i%4==0 and i%9==0:
        print(i)
