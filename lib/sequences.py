#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print([])  # If the length is less than or equal to 0, return an empty list
        return
    
    fibonacci_sequence = [0, 1]  # Starting values for the Fibonacci sequence

    # Generate the Fibonacci sequence up to the desired length
    for i in range(2, length):
        next_fib = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_fib)
    
    # If the requested length is 1, adjust the output accordingly
    if length == 1:
        fibonacci_sequence = [0]

    print(fibonacci_sequence)