# Class Method- bound to class and not with instance of class

class Employee:
    company="Apple"
    def show(self):
        print("Name is",self.name,"and company name is : ",self.company)

    @classmethod
    def changecompany(cls,newcompany):
        cls.company=newcompany

emp1=Employee()
emp2=Employee()
emp1.name="Anik"
emp1.changecompany("Samsung")
emp1.show()
print(Employee.company)

