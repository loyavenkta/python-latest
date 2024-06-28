inventory_name = ['screws', 'wheels', 'Metal', 'Rubber', 'Scredrivwe','woood']
inventory_numbers = [43,12,95,421,23,43]
"""print(list(zip(inventory_name,inventory_numbers)))"""
"""for name,number in zip(inventory_name,inventory_numbers):
    print(f'{name} current inventory : {number}')
for index, thing in enumerate(inventory_name):
    print(f'{index} : {thing}')
    if index == len(inventory_name) // 2:
        print("half way done")"""


for index, inventory_tuple in enumerate(zip(inventory_name,inventory_numbers)):
    print(f'{inventory_tuple[0]} [id : {index}] - inventor: {inventory_tuple[1]}')