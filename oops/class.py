#make a class and object
class Employee:
    name = "John"
    work = "devolopment"
    salary = 10000
emp1=Employee()
print(emp1.work)
emp1.work = "testing"
print(emp1.work)
print(emp1.salary)
print(Employee.work)