import csv
class log_reg:
    #Registration block
    def Registration(self):
        self.user_name=str(input("Enter the user name:"))
        self.pswrd=input("New Password:")
        self.phno=int(input("Enter your phone number:"))
        self.pin_code=int(input(("Enter your pincode:")))
        self.city=input("Enter your city:")
        with open("User_registration.csv","a",newline="") as file:
                          store=csv.writer(file)
                          store.writerow([self.user_name,self.pswrd,self.phno,self.pin_code,self.city])
                          file.close()        
        print("Registration Successful!!,Welcome to the Masters Work Family!!!!")
    #login block
    def Log_in(self):
        print("Hey")
        self.name_input=input("Enter User Name:")
        self.pswrd_input=input("Enter The Password:")
        log_in_status=0
        with open("User_registration.csv","r",newline="") as file:
            read=csv.DictReader(file)
            for row in read:
                if self.name_input==row['user_name'] and self.pswrd_input==row['pswrd']:
                    print("Log in successful!!!!")
                    log_in_status=1
            if log_in_status!=1:
                print("Invalid credentials!!!!!!!")
                self.Log_in()
'''
#checking the module
obj=log_reg()
print("Enter your choice:")
choice=int(input())
if choice==1:
    obj.Registration()
else:
    obj.Log_in() '''


    

        
        
        
                        
