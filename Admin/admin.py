class Admin:
    def __init__(self,package_id,package_name,price,start_date,end_date,duration):
        self.package_id = package_id
        self.package_name = package_name
        self.price = price
        self.start_date = start_date
        self.end_date = end_date
        self.duration = duration

    def __str__(self):
        return str(self.package_id)+","+self.package_name +","+str(self.price)+","+str(self.start_date)+","+str(self.end_date)+","+str(self.duration)+"days"+"\n"   