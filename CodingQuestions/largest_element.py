def find_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

# Optional

#def find_largest2(numbers):
    #return max(numbers)

nums = [3,1,6,8,5,15,20,14]
largest_num = find_largest(nums)
print(f"The largest number is {largest_num}.")        