class PowerCalculator:
    def my_pow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n

        result = 1
        while n:
            if n % 2:
                result *= x
            x *= x
            n //= 2

        return result

# Example usage:
# Create an instance of PowerCalculator class
calculator = PowerCalculator()

# Test the my_pow method
base = float(input("Enter the base (x): "))
exponent = int(input("Enter the exponent (n): "))

result = calculator.my_pow(base, exponent)
print(f"The result of {base}^{exponent} is: {result}")
