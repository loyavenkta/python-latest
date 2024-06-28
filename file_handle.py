file = open('test.txt')
print(list(file))
file.close()
 

""" #3# open or close txt file automatically
with open("test.txt") as file:
    for i in list(file):
        print(i)"""

with open('test.txt', 'a') as file:
    file.write("###################KALKI BLOCKBUSTER OPENING ###############")


with open('test copy.txt', 'w') as file:
    file.write( '''        
                           *
                         *****
                       *********
                    ****************  
                            #         
                            #
                            #
                            #
                            #           ''')