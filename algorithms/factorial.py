class Factorial:
    """Get factorial from n"""

    def __init__(self, n: int) -> None:
        assert type(n) is int, "n should be an integer"
        assert n >= 0, "Enter positive numbers only"

        self.n: int = n

    def iterate_factorial(self) -> int:
        """
        Obtain the factorial by iterating the n elements, e.g.
        5! = 5 * 4 * 3 * 2 * 1 = 120
        :return: factorial of the value n
        """
        if self.n == 1:
            return self.n

        if self.n == 0:
            return 1

        fact: int = 1

        for i in range(2, self.n + 1):
            fact *= i

        return fact

    def recur_factorial(self) -> int:
        """
        Get factorial of value n using recursion, e.g
        n! = n(n-1)
        !5 = 5 * 4!
        :return: factorial of the value n
        """
        if self.n == 1:
            return self.n

        if self.n == 0:
            return 1

        recur: int = Factorial(n=self.n - 1).recur_factorial()

        return recur * self.n
