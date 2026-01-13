from functools import reduce

for i in range(21):
    print(i)

even = lambda x: x % 2 == 0

num = range(1, 21)

even_num = list(filter(even, num))

print(even_num)

numbers = range(1, 21)

even = lambda x: x % 2 == 0

even_numbers = list(filter(even, numbers))

squared_evens = list(map(lambda x: x**2, even_numbers))

sum_of_squares = reduce(lambda a, b: a + b, squared_evens)

for index, value in enumerate(squared_evens):
    print(index, value)

print("Sum of squared even numbers:", sum_of_squares)
