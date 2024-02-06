def count_frequency(numbers):
    frequency = {}
    for num in numbers:
        if num in frequency:
            frequency[num] +=1
        else:
            frequency[num] = 1
    return frequency

# Test
nums = [1,2,3,1,3,4,5,2,5,6,3]
frequency_count = count_frequency(nums)
print(f"The frequency of the numbers is {frequency_count}.")             
