def square_numbers(numbers):
    return list(map(lambda x: x**2, numbers))

# Test
numbers = [1, 2, 3, 4, 5]
result = square_numbers(numbers)
print(result)