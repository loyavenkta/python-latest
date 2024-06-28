"""x = 0
while x<10 :
    x += 1
    if x == 8:
        continue

    print(x)"""

practise = [[10,40,29,50],[2,3,4,55],[101,20,32,43]]
for i in practise:
    for j in i:
        if j > 100:
            if j > 50 and j < 10:
                print(j)
    j = j+1 
