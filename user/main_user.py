from user_operations import UserOperations
def umain():
    u = UserOperations()
    ch = 0
    while True:
        try:
            print("\n***Explore Your Options***")
            print("\t1.View Packages")
            print("\t2.Search Packages")
            print("\t3.Booking")
            print("\t4.Exit")
            ch = int(input("Enter the your choice: "))
            if(ch == 1):
                u.view_packages()
            elif(ch == 2):
                package_name = input("Enter the place name do you want to explore: ").lower()
                u.search_package(package_name)
            elif(ch == 3):
                u.booking()
            elif(ch == 4):
                print("Thank you for exploring our side.\nHope you like it,Visit again!!!")
                break
            else:
                print("Invalid choice. Please enter a valid option.")
                break
        except ValueError:
            print("Please enter only numric values.")
if (__name__ == "__main__"):
    umain()