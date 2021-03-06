# Problem 2:
# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose
# values do not exceed four million, find the sum of the even-valued terms.

import itertools

class FibonacciSequence:

    def __init__(self):
        self.Fn_2 = 0
        self.Fn_1 = 1
        self.Fn = 1

    def __repr__(self):
        return f"Fibonacci(0,1,...,{self.Fn})"

    def __iter__(self):
        while True:
            yield self.Fn
            self.Fn_2 = self.Fn_1
            self.Fn_1 = self.Fn
            self.Fn = self.Fn_1 + self.Fn_2


def problem002():
    total = 0
    for i in itertools.takewhile(lambda f: f < 4_000_000, FibonacciSequence()):
        if i % 2 == 0:
            total += i
    return total