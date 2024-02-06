def filter_positive_numbers(numbers):
    positives = list(filter(lambda x: x > 0, numbers))
    return positives

# Test
numbers = [-1, 2, -3, 4, -5]
positive_numbers = filter_positive_numbers(numbers)
print(positive_numbers)