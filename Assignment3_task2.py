import math

try:
    num = float(input("Enter a number: "))
    if num < 0:
        print("Error: Square root and natural log are not defined for negative numbers.")
    elif num == 0:
        print("Error: Natural log is not defined for zero.")
    else:
        sqrt_value = math.sqrt(num)

        log_value = math.log(num)

        sin_value = math.sin(num)
        print(f"Square root of {num}: {sqrt_value}")
        print(f"Natural logarithm (log base e) of {num}: {log_value}")
        print(f"Sine of {num} (in radians): {sin_value}")

except ValueError:
    print("Error: Please enter a valid number.")