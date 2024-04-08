class User:
    def __init__(self,username,package_id,package_name,no_persons):
        self.username = username
        self.package_id = package_id
        self.package_name = package_name
        self.no_persons = no_persons

    def __str__(self):
        return self.username+ ","+str(self.package_id)+","+self.package_name +","+str(self.no_persons)+"\n"
    

