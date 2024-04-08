from user import User
from datetime import datetime
import ex
class UserOperations:
    #view availavble tour packages
    def view_packages(self):
        fp = ex.read_file("Admin/package_details.txt")
        #with open("Admin/package_details.txt","r")as fp:
        if fp is not None:
            for line in fp:
                sep_text = line.split(',')
                print(f"\tPackage of {sep_text[1].capitalize()}\n")
                print(f"\t\tPackage ID : {sep_text[0]}")
                print(f"\t\tPackage Name : {sep_text[1].capitalize()}")
                print(f"\t\tPackage Price : {sep_text[2]}/person")
                print(f"\t\tDept. Date : {sep_text[3]} --> {sep_text[4]}")
                print(f"\t\tPackage Duration : {sep_text[5]}")
                print("______________________________________________________________________")
        
    #serach package by package name
    def search_package(self,package_name):
        found = False
        fp = ex.read_file("Admin/package_details.txt")
        #with open("Admin/package_details.txt", "r") as fp:
        if fp is not None:
            for line in fp:
                sep_text = line.split(',')
                if len(sep_text) >= 2 and sep_text[1].strip() == package_name:
                    found = True
                    print(f"Details for {package_name} Tour :\n")
                    self.showinfo(sep_text)    
        if found != True:
            print("Sorry tour is not available for this place.")

    #Package booking
    def booking(self):
        username = input("Please give your good name: ")
        package_id = int(input("Enter the package_id: "))
        package_name = input("Enter the package name: ")
        price = self.find_package_details(package_id,package_name)
        gst = 0.05
        grand_total = 0
        
        if price:
            no_of_persons = int(input("For how many peoples do you want to book tour: "))
            book_user = User(username,package_id,package_name,no_of_persons)
            sub_total = price* no_of_persons
            gst_amount = sub_total * gst
            grand_total = sub_total + gst_amount

            with open("user/user_details.txt","a") as fp:
                fp.write(str(book_user))

            print("You need to pay this amount Rs.",grand_total,"(Including Gst)")
            user_input = input("Do you want to print invoice(y/n):\n ")
            if user_input.lower() == 'y':
                self.bill(grand_total,sub_total,gst_amount,price)
                print("Your tour is booked.") 
        else:
            print("Sorry Package not Found.Please try again.\n Please use other available options to get right information.")   
    
    #Chech package is available or not. also return price
    def find_package_details(self,package_id,package_name):
        fp = ex.read_file("Admin/package_details.txt")
        # with open("Admin/package_details.txt", "r") as fp:
        if fp is not None:
            for line in fp:
                sep_text = line.split(',')
                if int(sep_text[0]) == package_id and sep_text[1].strip() == package_name:
                    price = int(sep_text[2])
                    return price
        return

    def showinfo(self,sep_text):
        print(f"\t\tPackage ID : {sep_text[0]}")
        print(f"\t\tPackage Name : {sep_text[1].capitalize()}")
        print(f"\t\tPackage Price : {sep_text[2]}/person")
        print(f"\t\tDept. Date : {sep_text[3]} --> {sep_text[4]}")
        print(f"\t\tPackage Duration : {sep_text[5]}")
        print("**NOTE**")
        print("\tTerms and Conditions apply.")
        print(f"\t5% GST is applicable on given tour price.")
    
    def bill(self,grand_total,sub_total,gst_amount,price):
        fp = ex.read_file("user/user_details.txt")
        # with open("user/user_details.txt","r") as fp:
        if fp is not None:
            for line in fp:
                    sep_user = line.split(',')
        
        print("\t\t\t\tINVOICE")
        print(f"Invoive To:{sep_user[0]}")
        print(f"Invoice Date :{datetime.now().date()}")
        print("_________________________________________________________________")
        print("package name \tNo persons \tU.Price \tAmount")
        print("__________________________________________________________________")
        print(f"{sep_user[2].capitalize()} \t\t{sep_user[3]}        \t\t\t{price}\t\t{sub_total}")
        print("__________________________________________________________________")
        print(f"\t\t\t\tSub Total\t{sub_total}")
        print(f"\t\t\t\tTax Amount(5%)\t{gst_amount}")
        print(f"\t\t\t\tGrand Total\t{grand_total}")