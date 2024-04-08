from admin import Admin
from datetime import datetime
import ex
class Operations:
    #To view available packages
    def view_packages(self):
        fp = ex.read_file("Admin/package_details.txt")
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

    #To add the packages
    def add_packages(self):
        package_id = int(input("Enter package id: "))
        package_name = input("Enter package name: ").lower()
        price = int(input("Enter package price: "))
        start_date = input("Enter a start date (YYYY-MM-DD):")
        end_date = input("Enter a end date (YYYY-MM-DD): ")

        if not ex.valid_date(start_date) or not ex.valid_date(end_date):
            print("Error: Please enter valid dates within the current year and today or a future date.")
            return
        try:
            duration = self.date_difference(start_date,end_date)
            start_date ,end_date = self.dateconversion(start_date,end_date)
        except ValueError:
            print("Error: Please enter valid date formats.")
            return
        
        package = Admin(package_id,package_name,price,start_date,end_date,duration)

        with open("Admin/package_details.txt","a") as fp:
            fp.write(str(package))
            print("Package added succesfully.")

    # To remove the package
    def remove_package(self, id):
        found = False
        lines = []
        fp = ex.read_file("Admin/package_details.txt")
        # with open("Admin/package_details.txt", "r") as fp:
        if fp is not None:
            for line in fp:
                sep_text = line.split(',')
                if sep_text[0] == str(id):
                    found = True
                    print(f"Package with ID {id} found and removed successfully.")
                else:
                    lines.append(line)

        if found:
            with open("Admin/package_details.txt", "w") as fp:
                fp.writelines(lines)
        else:
            print(f"No package found with ID {id}. Nothing removed.")

    #To update package details
    def update_package(self, id):
        found = False
        updated_lines = []
        fp = ex.read_file("Admin/package_details.txt")
        # with open("Admin/package_details.txt", "r") as fp:
        if fp is not None:
            for line in fp:
                sep_text = line.split(',')
                if sep_text[0] == str(id):
                    found = True
                    self.update_data(sep_text)
                    line = ','.join(map(str, sep_text))
                updated_lines.append(line)
        if found:
            with open("Admin/package_details.txt", "w") as fp:
                fp.writelines(updated_lines)
                print("File updated successfully.")
        else:
            print(f"No package found with ID {id}.")

    #To view bookings package wise
    def view_booking(self):
        booking = {}
        fp = ex.read_file("user/user_details.txt")
        # with open("user/user_details.txt","r") as fp:
        if fp is not None:
            for line in fp:
                sep_text = line.split(",")
                if sep_text[2] not in booking:
                    booking[sep_text[2]] = 1
                else:
                    booking[sep_text[2]] += 1
        print("\t\tBooking Summary")
        print("____________________________________________")
        print("\tPackage Name  |\tBooking Count")
        print("____________________________________________")
        for package_name , count in booking.items():
            print(f"\t{package_name.capitalize()}  \t {count}")
        print("____________________________________________")

    #data updatation parameter
    def update_data(self, sep_text):
        name = input("Do you want to update the package name (y/n): ")
        if name.lower() == 'y':
            sep_text[1] = input("Enter the new package name: ").lower()

        price = input("Do you want to update the price (y/n): ")
        if price.lower() == 'y':
            sep_text[2] = int(input("Enter the new package price: "))
            
        date = input("Do you want to update the date (y/n): ")
        if date.lower() == 'y':
            start_date = input("Enter a start date (YYYY-MM-DD):")
            end_date = input("Enter a end date (YYYY-MM-DD): ") 

            if not ex.valid_date(start_date) or not ex.valid_date(end_date):
                print("Error: Please enter valid dates within the current year and today or a future date.")
                return
            try:
                duration = self.date_difference(start_date,end_date)
                start_date , end_date = self.dateconversion(start_date,end_date)
            except ValueError:
                print("Error:Please enter valid date formats.")
                return
            
            sep_text[3] = start_date
            sep_text[4] = end_date
            sep_text[5] = str(duration) +"days"

    #Date Conversion
    def dateconversion(self,start_date,end_date):
        converted_sd= datetime.strptime(start_date,"%Y-%m-%d")
        converted_ed = datetime.strptime(end_date,"%Y-%m-%d")
        format_sd = converted_sd.strftime("%d-%B-%Y")
        format_ed = converted_ed.strftime("%d-%B-%Y")
        return format_sd,format_ed
        
    #Duration calculation
    def date_difference(self,start_date,end_date):
        converted_sd= datetime.strptime(start_date,"%Y-%m-%d")
        converted_ed = datetime.strptime(end_date,"%Y-%m-%d")
        diff = converted_ed - converted_sd
        return diff.days