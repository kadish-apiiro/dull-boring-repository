class Calculator:
    """
    A simple calculator class that performs basic arithmetic operations.
    """

    def add(self, a, b):
        """
        Adds two numbers.

        Args:
            a (int or float): The first number.
            b (int or float): The second number.

        Returns:
            int or float: The sum of a and b.
        """
        return a + b

    def subtract(self, a, b):
        """
        Subtracts the second number from the first.

        Args:
            a (int or float): The first number.
            b (int or float): The second number.

        Returns:
            int or float: The difference between a and b.
        """
        return a - b

    def multiply(self, a, b):
        """
        Multiplies two numbers.

        Args:
            a (int or float): The first number.
            b (int or float): The second number.

        Returns:
            int or float: The product of a and b.
        """
        return a * b

    def divide(self, a, b):
        """
        Divides the first number by the second.

        Args:
            a (int or float): The first number.
            b (int or float): The second number.

        Returns:
            float: The quotient of a and b.

        Raises:
            ValueError: If b is zero.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

def main():
    calc = Calculator()
    print("Welcome to the Boring Calculator.")
    print(f"1 + 1 = {calc.add(1, 1)}")
    print(f"5 - 2 = {calc.subtract(5, 2)}")
    print(f"3 * 4 = {calc.multiply(3, 4)}")
    print(f"10 / 2 = {calc.divide(10, 2)}")

if __name__ == "__main__":
    main()

