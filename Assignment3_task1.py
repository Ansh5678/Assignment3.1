def factorial(n):


    if n < 2:
          return 1
    else:
          return n*factorial(n-1)

if __name__ == "__main__":
    try:
        sample_number = int(input("Enter a  integer: "))
        result = factorial(sample_number)
        print(result)
    except ValueError as e:
        print(f"Error: {e}. Please enter a  integer.")
