

def fibonacci(number):
    fibonacci_numbers = [0, 1]
    total = 1

    for index in range(2, number+1):
        total = (
            fibonacci_numbers[-2] +
            fibonacci_numbers[-1]
        )
        fibonacci_numbers.append(total)

    return total

def fibonacci_1(number):
    if number <= 1:
        return number
    
    return fibonacci_1(number - 2) + fibonacci_1(number - 1)
