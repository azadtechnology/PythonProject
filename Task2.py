import math

# TASK 2
try:
    number = float(input("Enter a number: "))

    if number < 0:
        print("Square root and logarithm are not defined for negative numbers.")
    elif number == 0:
        print("Square root:", math.sqrt(number))
        print("Natural logarithm is undefined for zero.")
        print("Sine:", math.sin(number))
    else:
        # Calculate values using the math module
        sqrt_val = math.sqrt(number)
        log_val = math.log(number)
        sine_val = math.sin(number)
        
        print(f"Square root: {sqrt_val}")
        print(f" logarithm: {log_val}")
        print(f"Sine: {sine_val}")

except ValueError:
    print("Invalid input! Please enter a valid number.")
