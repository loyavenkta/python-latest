
"""
x = input("what is x?")
y = input("what is y?")
#z = int(x)+ int(y) 
k = round(float(x) + float(y))

print(f"{k:,}")
"""


def main():
    x = int(input("what is x? "))
    print(f"{x} squared is ",square(x))
def square(n):
    return n*n
main()



