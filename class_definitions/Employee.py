"""
Author:  Derek Bittner

Program:  Encapsulation assignment
"""
from datetime import date


class Employee:
    """Employee class"""

    #Constructor
    def __init__(self, lname, fname, address, pnumber, salaried, sdate, salary):
        self.last_name = lname
        self.first_name = fname
        self.address = address
        self.phone_number = pnumber
        self.salaried = salaried
        self.start_date = sdate
        self.salary = salary

    def display(self):
        if self.salaried:
            return self.first_name + " " + self.last_name + "\n"\
                + self.address + "\n" + self.phone_number + "\n"\
                + "Salaried employee: $" + str(self.salary) + "/year" + "\n" + str(self.start_date)
        else:
            return self.first_name + " " + self.last_name + "\n"\
                + self.address + "\n" + self.phone_number + "\n"\
                + "Hourly employee: $" + str(self.salary) + "/hour" + "\n" + str(self.start_date)

    def __str__(self):
        return 'Employee: first name = ' + str(self.first_name) + " " + str(self.last_name) + "\n"\
                + str(self.address) + "\n" + str(self.phone_number) + "\n"\
                + "Salaried employee: $" + str(self.salary) + "/year" + "\n" + str(self.start_date)


# Drive
tdate = date.today()
empl = Employee("Bittner", "Derek", "123 nowhere st., Chariton, IA 50909", "123-123-1234", True, tdate, 39000)
print(empl.display())
print(empl)

empl2 = Employee("Bittner", "Joe", "123 nowhere st., Chariton, IA 50909", "123-123-1234", False, tdate, 7.50)
print(empl2.display())
print(repr(empl2))
