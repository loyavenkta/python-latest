"""x = [ ]
value = 0
while value <= 100:
    if value % 2 == 0 and value != 58:
        x.append(value)
    value += 1
print(x)"""

"""basic_list = [1,2,3]
for x in basic_list:
    print(x)"""


practise = [[10,40,29,50],[2,3,4,55],[101,20,32,43]]
for i in practise:
    for j in i:
        if j > 100:
            break
        if j < 50 and j > 10:
            print(j)



