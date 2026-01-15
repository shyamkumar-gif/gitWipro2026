# iterators
class NumberIterator:
    """iterator that iterates from 1 to N"""
    def __init__(self, n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.n:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration


def fibonacci_generator(n):
    """Generator for first N Fibonacci numbers"""
    a, b = 0, 1
    count = 0

    while count < n:
        yield a
        a, b = b, a + b
        count += 1


# difference between iterator and generator
if __name__ == "__main__":
    print("Iterator Output:")
    iterator = NumberIterator(5)
    for num in iterator:
        print(num)

    print("\nGenerator Output:")
    for fib in fibonacci_generator(5):
        print(fib)
