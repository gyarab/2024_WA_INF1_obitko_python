class InputError(Exception):
    pass

def fibonacci(n):
    if not isinstance(n, int) or n < 0:
        raise InputError("Invalid input. Please provide a positive integer.")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib_sequence = [0, 1]
        for i in range(2, n):
            fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
        return fib_sequence[-1]

try:
    print(fibonacci(10))
except InputError as e:
    print(e)