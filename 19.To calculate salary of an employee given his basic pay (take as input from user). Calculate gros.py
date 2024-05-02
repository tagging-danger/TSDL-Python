class EmployeeSalaryCalculator:
    def __init__(self, basic_pay):
        self.basic_pay = basic_pay
        self.hra_percentage = 0.10
        self.ta_percentage = 0.05
        self.professional_tax_percentage = 0.02

    def calculate_gross_salary(self):
        hra = self.basic_pay * self.hra_percentage
        ta = self.basic_pay * self.ta_percentage
        gross_salary = self.basic_pay + hra + ta
        return gross_salary

    def calculate_professional_tax(self, gross_salary):
        professional_tax = gross_salary * self.professional_tax_percentage
        return professional_tax

    def calculate_net_salary(self, gross_salary, professional_tax):
        net_salary = gross_salary - professional_tax
        return net_salary

# Take basic pay as input from the user
basic_pay = float(input("Enter the basic pay of the employee: "))

# Create an instance of EmployeeSalaryCalculator
calculator = EmployeeSalaryCalculator(basic_pay)

# Calculate gross salary
gross_salary = calculator.calculate_gross_salary()

# Calculate professional tax
professional_tax = calculator.calculate_professional_tax(gross_salary)

# Calculate net salary
net_salary = calculator.calculate_net_salary(gross_salary, professional_tax)

# Display the results
print(f"\nBasic Pay: {basic_pay}")
print(f"Gross Salary: {gross_salary}")
print(f"Professional Tax: {professional_tax}")
print(f"Net Salary: {net_salary}")
