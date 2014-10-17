class Employee:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def getName(self):
        return self.firstName + " " + self.lastName


class HourlyEmployee(Employee):
    def __init__(self, firstName, lastName, hourlyWage):
        super().__init__(firstName, lastName)
        self.hourlyWage = hourlyWage

    def calculateCash(self, workHours):
        return workHours * self.hourlyWage


class SalariedEmployee(Employee):
    def __init__(self, firstName, lastName, annualSalary):
        super().__init__(firstName, lastName)
        self.annualsalary = annualSalary

    def calculateCash(self, workHours):
        return self.annualsalary


class Manager(SalariedEmployee):
    def __init__(self, firstName, lastName, annualSalary, bonus):
        super().__init__(firstName, lastName, annualSalary)
        self.bonus = bonus

    def calculateCash(self, workHours):
        return self.annualsalary + self.bonus


staff = []
staff.append(HourlyEmployee("Morgan", "Harry", 30.0))
staff.append(SalariedEmployee("Lin", "Sally", 52000.0))
staff.append(Manager("Smith", "Mary", 104000.0, 50.0))
for employee in staff:
    hours = int(input("Hours worked by " + employee.getName() + ": "))
    pay = employee.calculateCash(hours)
    print("Salary: %.2f" % pay)
