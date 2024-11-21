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