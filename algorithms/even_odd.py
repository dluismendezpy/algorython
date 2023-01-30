"""
Given an integer, n, perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of  to , print Not Weird
If n is even and in the inclusive range of  to , print Weird
If n is even and greater than , print Not Weird
"""


class EvenOdd:
    """
    Takes an integer as input and returns whether it's "Weird" or "Not Weird" based on certain conditions.
    """

    def __init__(self, n: int):
        """
        Initialize the class with the input integer.
        :param int n: input integer
        """
        if not isinstance(n, int):
            raise ValueError("Input must be an integer.")
        self.n = n

    def calculate_weirdness(self) -> str:
        """
        Calculate and return whether the input integer is "Weird" or "Not Weird".
        """
        if self.n % 2 != 0 or (6 <= self.n <= 20):
            return "Weird"
        else:
            return "Not Weird"
