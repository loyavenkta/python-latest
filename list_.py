list2 = [('a',3),('b',10),('c',6),('d',5)]
def sort_fun(item):
    return item[1]

print(sorted(list2, key = sort_fun))
print(sorted(list2, key = lambda item: item[1]))

inventory_name = ['screws', 'wheels', 'Metal', 'Rubber', 'Scredrivwe','woood']
inventory_numbers = [43,12,95,421,23,43]
combined_list = list(zip(inventory_name,inventory_numbers))
print(sorted(combined_list, key = lambda inv_tuple: inv_tuple[1]))
print(sorted(combined_list,key= lambda inv_tuple : len(inv_tuple[0])))


my_list = [1,2,3,4,5]
print(list(map(lambda num : num**2,my_list)))

print([num**2 for num in my_list])


print(list(filter(lambda num : num <4, my_list)))
print([num for num in my_list if num <4])

