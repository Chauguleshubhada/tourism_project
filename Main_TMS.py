from Admin.admin_main import amain
from user.main_user import umain
def main():
    ch = 0
    while True:
        try:
            print("\n***Select Your Options***")
            print("\t1.Admin Login")
            print("\t2.User Login")
            print("\t3.Exit")
            ch = int(input("Enter the your choice: "))
            if(ch == 1):
                amain()
            elif(ch == 2):
                umain()
            elif(ch == 3):
                break
            else:
                print("Invalid choice. Please enter a valid option.")
                break
        except ValueError:
            print("Please enter only numric values.")
if (__name__ == "__main__"):
    main()