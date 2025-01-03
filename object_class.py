class employ:
    def employData(self):
        self.id= input("ENTER THE EMPLOY ID (000-000-ABC) : ")
        self.name =input("ENTER THE EMPLOY NAME : ")
        self.salary =float(input("ENTER THE SALARY (000.00) : "))
    def display(self) :
        print("EMPLOY ID IS : ",self.id)
        print("EMPLOY NAME IS : ",self.name)
        print("EMPLOY SALARY IS : ",self.salary)
#main
a = employ()
a.employData()
a.display()
b = employ()
b.employData()
b.display()