def find_second_largest(nums):
    if len(nums) < 2:
        return "List must have at least two elements"
    
    largest = float('-inf')
    second_largest = float('-inf')
    
    for num in nums:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    return second_largest

# Test
nums = [1, 3, 2, 5, 4, 10, 15]
result = find_second_largest(nums)
print("Second largest element:", result)
