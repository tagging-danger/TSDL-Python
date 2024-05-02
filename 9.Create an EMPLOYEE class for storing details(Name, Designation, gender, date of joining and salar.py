class Employee:
    total_employees = 0
    male_count = 0
    female_count = 0
    high_salary_count = 0
    manager_count = 0

    def __init__(self, name, designation, gender, join_date, salary):
        self.name = name
        self.designation = designation
        self.gender = gender
        self.join_date = join_date
        self.salary = salary

        # Update class variables
        Employee.total_employees += 1
        if gender.lower() == 'male':
            Employee.male_count += 1
        elif gender.lower() == 'female':
            Employee.female_count += 1

        if salary > 10000:
            Employee.high_salary_count += 1

        if designation.lower() == 'manager':
            Employee.manager_count += 1

    @classmethod
    def display_employee_statistics(cls):
        print("\nEmployee Statistics:")
        print("Total Employees:", cls.total_employees)
        print("Male Employees:", cls.male_count)
        print("Female Employees:", cls.female_count)
        print("Employees with Salary > 10,000:", cls.high_salary_count)
        print("Managers:", cls.manager_count)

# Function to take input for a single employee
def get_employee_details():
    name = input("Enter employee name: ")
    designation = input("Enter employee designation: ")
    gender = input("Enter employee gender: ")
    join_date = input("Enter employee join date (YYYY-MM-DD): ")
    salary = float(input("Enter employee salary: "))
    return name, designation, gender, join_date, salary

# Example usage:
num_employees = int(input("Enter the number of employees: "))

for _ in range(num_employees):
    emp_details = get_employee_details()
    emp = Employee(*emp_details)

# Display employee statistics after input
Employee.display_employee_statistics()
