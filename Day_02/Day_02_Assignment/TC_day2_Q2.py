# descriptors.py

class PositiveSalary:
    #Descriptor to ensure salary is always positive
    def __get__(self, instance, owner):
        return instance.__dict__.get("salary")

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("Salary must be a positive number")
        instance.__dict__["salary"] = value


class Employee:
    salary = PositiveSalary()

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


# descriptor
if __name__ == "__main__":
    emp1 = Employee("Alice", 50000)
    emp2 = Employee("Bob", 70000)

    print(emp1.name, emp1.salary)
    print(emp2.name, emp2.salary)
# I kept tha terror in a try block so that the code executes without errors but gave a statement to show the error
    try:
        emp3 = Employee("Charlie", -30000)
    except ValueError as e:
        print("Error:", e)

