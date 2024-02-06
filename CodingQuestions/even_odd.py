# List comprehension version
def check_even_odd(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]
    return even_numbers, odd_numbers

'''
# Lambda version
def check_even_odd2(numbers):
    is_even = lambda x: x % 2 == 0
    is_odd = lambda x: x % 2 !=0
    even = list(filter(is_even, numbers))
    odd = list(filter(is_odd, numbers))
    return even, odd
'''

# Test
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even, odd = check_even_odd(numbers)
print("Even numbers:", even)
print("Odd numbers:", odd)