# prime_number_checker.py

from prime_checker import PrimeChecker  # Importing the PrimeChecker class from prime_checker.py

class NumberValidator:
    def __init__(self):
        self.prime_checker = PrimeChecker()  # Create an instance of the PrimeChecker class

    def validate(self, n):
        if self.prime_checker.is_prime(n):
            print(f"{n} is a prime number")
        else:
            print(f"{n} is not a prime number")

# Example usage:
if __name__ == "__main__":
    validator = NumberValidator()
    number = int(input("Enter a number: "))
    validator.validate(number)
