from log_regs import *
import csv
#from products import *
class home_page:
    def welcome(self):
        print("Welcome to world's best E-Commerce Website!!!!!!!")
        print("Select the option from below:\n1.Registration \n2.Log_in")
        log_choice=input()
        if log_choice=="1" or log_choice== "Registration" or log_choice== "registration":
            obj1.Registration()
        elif log_choice=="2" or log_choice== "Log_in" or log_choice== "log_in":
            obj1.Log_in()
        else:
            print("Invalid Response!!!!")
            self.welcome()
'''with open("User_registration.csv","a",newline="") as file1:
                          varsd=csv.writer(file1)
                          varsd.writerow(["user_name","pswrd","phno","pin_code","city"])
                          file1.close()             '''
obj1=log_reg()
obj=home_page()
obj.welcome()

    