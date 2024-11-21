class InputError(Exception):
    pass

def fibonacci(index):
    if not isinstance(index, int) or index < 0:
        raise InputError("Invalid input. Please provide a non-negative integer.")
    elif index == 0:
        return 0
    elif index == 1:
        return 1
    else:
        fib_sequence = [0, 1]
        for i in range(2, index + 1):
            fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
        return fib_sequence[index]

try:
    print(fibonacci(0))  
except InputError as e:
    print(e)