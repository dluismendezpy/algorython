from math import factorial

from .factorial import Factorial


class Permutation:
    """Permutations (Pn) using recursion and iteration"""

    def __init__(
        self,
        combination: str,
        pocket: str = "",
        iterate_str: list[str] | None = None,
    ) -> None:
        assert (
            type(combination) is str
        ), "combination param should be a str instance"
        assert type(pocket) is str, "pocket param should be a str instance"

        self.combination: str = combination
        self.pocket: str = pocket
        self.iterate_str: list[str] = iterate_str

    def iterate_permute(self) -> None:
        """
        Get permute of iterate_str param using iteration, e.g
        Pn "ABC" = !3 = 6.
        :return: all permutations from iterate_str param
        """
        if self.iterate_str is None:
            return

        iterate_str_len = len(self.iterate_str)
        fact: Factorial = Factorial(n=iterate_str_len)
        print(f"\nNumber of combinations: {fact.iterate_factorial()}")

        for p in range(factorial(iterate_str_len)):
            print("".join(self.iterate_str))

            i: int = iterate_str_len - 1

            while i > 0 and self.iterate_str[i - 1] > self.iterate_str[i]:
                i -= 1

            self.iterate_str[i:] = reversed(self.iterate_str[i:])

            if i > 0:
                q: int = i

                while self.iterate_str[i - 1] > self.iterate_str[q]:
                    q += 1

                temp: str = self.iterate_str[i - 1]
                self.iterate_str[i - 1] = self.iterate_str[q]
                self.iterate_str[q] = temp

    def recur_permute(self) -> None:
        """
        Get permute of combination param using recursion, e.g
        Pn "ABC" = !3 = 6.
        :return: all permutations from combination param
        """
        combination_len: int = len(self.combination)

        if combination_len == 0:
            print(self.pocket)

        for p in range(combination_len):
            letter: str = self.combination[p]

            # Join first + last letter
            word: str = self.combination[:p] + self.combination[p + 1 :]

            permutation: Permutation = Permutation(
                combination=word, pocket=letter + self.pocket
            )
            permutation.recur_permute()
