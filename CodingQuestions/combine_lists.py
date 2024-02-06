def combine_lists(list1, list2):
    combined = list(zip(list1, list2))
    return combined

# Test
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
combined_list = combine_lists(list1, list2)
print(combined_list)