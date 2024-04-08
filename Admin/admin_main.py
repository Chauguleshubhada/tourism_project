from admin_oprations import Operations
def amain():
    op = Operations()
    ch = 0
    while True:
        print("\n*** Travel Package Management Menu ***")
        print("\t1.View Packages")
        print("\t2.Add Packages")
        print("\t3.remove Packages")
        print("\t4.update Packages")
        print("\t5.view booking")
        print("\t6.Exit")
        try:
            ch = int(input("Please Enter your choice: "))
            if(ch == 1):
                op.view_packages()
            elif(ch == 2):
                op.add_packages()
            elif(ch == 3):
                id = int(input("Enter the package ID:"))
                op.remove_package(id) 
            elif(ch == 4):
                id = int(input("Enter the package ID:"))
                op.update_package(id)
            elif(ch == 5):
                op.view_booking()
            elif(ch == 6):
                break
            else:
                print("Invalid choice. Please enter a valid option.")
                break
        except ValueError:
            print("Please enter only numric values[0-9].")
            
if(__name__== "__main__"):
    amain()