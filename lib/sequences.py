#!/usr/bin/env python3
def print_fibonacci(length):
    if length < 0:
        print("Please enter a positive integer")
        return

    fibonacci_sequence = []

    if length == 0:
        print(fibonacci_sequence)
        return

    a, b = 0, 1
    for _ in range(length):
        fibonacci_sequence.append(a)
        a, b = b, a + b

    print(fibonacci_sequence)

# example usage
print_fibonacci(10)
