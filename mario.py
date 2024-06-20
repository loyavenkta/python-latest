def main():
    mario_coloum()
    mario_row()
    mario_square(3)

def mario_coloum():
    print("#\n" * 3, end="")
    """for _ in range(3):
        print("#")"""
def mario_row():
    print("?\n" * 4, end="")

def mario_square(size):
    for i in range(size):
       for j in range(size):
           print("@", end="")
       print()


    

""" print(" @ " * 3, "\n", end ="" )
        i += 1"""


main()