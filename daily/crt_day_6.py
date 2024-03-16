print("DAY 6")
import csv
file=open("student.csv","a",newline="")
a=csv.writer(file)
#a.writerow(["Student name","roll No","Phone Number","roll Id"])

stud_name=input("Enter your name:")
stud_roll=int(input("Roll no:"))
stud_no=int(input("Phone number:"))
stud_id=int(input("student id:"))
a.writerow([stud_name,stud_roll,stud_no,stud_id])
print("Studetn record saved succesfully!!!")
file.close()
print()
with open("student.csv","r",newline="") as file:
    read=csv.DictReader(file)
    for row in read:
        print(row["roll Id"],row["Student name"])
file.close()
    


