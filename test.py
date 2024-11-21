def celsius_to_fahrenheit(celsius):
    if not isinstance(celsius, (int, float)):
        raise ValueError("Invalid input. Celsius must be a number.")
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    if not isinstance(fahrenheit, (int, float)):
        raise ValueError("Invalid input. Fahrenheit must be a number.")
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def fibonacci(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Invalid input. n must be a non-negative integer.")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_sequence = [0, 1]
        for i in range(2, n+1):
            fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
        return fib_sequence[n]  
    
def is_prime(number):
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Invalid input. Number must be a non-negative integer.")
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def primes_in_range(a, b):
    if not isinstance(a, int) or not isinstance(b, int) or a > b:
        raise ValueError("Invalid input. a and b must be integers and a must be less than or equal to b.")
    
    primes = []
    for num in range(a, b+1):
        if is_prime(num):
            primes.append(num)
    
    return primes

