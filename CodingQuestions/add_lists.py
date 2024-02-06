def add_lists(list1, list2):
    return [x + y for x,y in zip(list1, list2)]

# Test
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = add_lists(list1, list2)
print(result)