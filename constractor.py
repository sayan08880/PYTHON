class student :
    def __init__(self,a,b,c) :
        self.id = a
        self.name = b
        self.fees = c
    def display(self) :
        print(f"ID IS : ",self.id)
        print(f"NAME IS : ",self.name)
        print(f"FEES IS : ",self.fees)

sayan = student(1,"SAYAN",5000)
rahul = student(2,"RAJU",5000)
sayan.display()
rahul.display()