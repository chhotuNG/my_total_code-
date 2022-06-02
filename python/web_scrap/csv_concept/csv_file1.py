import csv 

def create():
    with open("detail.csv","w") as file1:
        fobj=csv.writer(file1)
        fobj.writerow(['roll','name','total_marks'])
        while True:
            roll=int(input("enter roll number___: "))
            name=input("enter student name__: ")
            total=int(input("enter total_marks of student___: "))
            record=[roll,name,total]
            fobj.writerow(record)
            ch1=input("if you want to add more press 1/2____: ")
            if ch1 == "2":
                break
def display():
    with open("detail.csv","r") as file1:
        obj=csv.reader(file1)
        for i in obj:
            print(i)
def search():
    with open("detail.csv","r") as file1:
        obj=csv.reader(file1)
        print(obj)
        for i in obj:
            print(i)   
create()
display()
search()


