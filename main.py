from algorithms.factorial import Factorial

if __name__ == "__main__":
    factorial: Factorial = Factorial(n=5)
    print(factorial.iterate_factorial())
    print(factorial.recur_factorial())
