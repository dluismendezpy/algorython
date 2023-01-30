# from algorithms.factorial import Factorial
# from algorithms.permutation import Permutation
from algorithms.even_odd import EvenOdd

if __name__ == "__main__":
    # region Factorial
    # factorial: Factorial = Factorial(n=5)
    # print(factorial.iterate_factorial())
    # print(factorial.recur_factorial())
    # endregion

    # region Permutation
    # permutation: Permutation = Permutation(
    #     combination="ABC", pocket="", iterate_str=list("123")
    # )
    # permutation.recur_permute()
    # permutation.iterate_permute()
    # endregion

    # region EvenOdd
    weirdness: EvenOdd = EvenOdd(n=5)
    print(weirdness.calculate_weirdness())
    # endregion
