"""my_list =[]
for num in range(0,100):
    my_list.append(num)
print(my_list)

my_list_comp = [(num,num,num)if num < 155 else 0 for num in range(100,199) ]
print(my_list_comp)"""

"""inventory_name = ['screws', 'wheels', 'Metal', 'Rubber', 'Scredrivwe','woood']
inventory_numbers = [43,12,95,421,23,43]
rep_list = [(name,number) for name, number in zip(inventory_name,inventory_numbers)if number <45]
print(rep_list)
"""

## combined_comp
chess_board = [[f'{letter}{num}' for num in range(1,9)]for letter in "ABCDEFGH"[::-1]]
for i in chess_board:
    print(i)

