# decorators.py

import time

def execution_time(func):
    #Decorator to measure execution time of a function
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' executed in {end_time - start_time:.6f} seconds")
        return result
    return wrapper


@execution_time
def factorial(n):
    #Recursive factorial function
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# applying decorator to a recursive function
if __name__ == "__main__":
    print("Factorial:", factorial(5))
