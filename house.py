"""name = str(input("what is your name? ").title()) 

if name == "Koushik":
    print("1804")
elif name == "sai":
    print("1803")
elif name == "Venkata":
    print("1801")
elif name == "loya":
    print("1802")
else:
    print("1")"""

# the difference between the two code are title() check first letter Cap.
## works in python 3.10
name = input("What is your name? ").title()
"""
match name:
    case "Koushik":
        print("1804")
    case "Sai":
        print("1803")
    case _:
        print("who?")
"""

if name == "Koushik":
    print("1804")
elif name == "Sai":
    print("1803")
elif name == "Venkata":
    print("1801")
elif name == "Loya":
    print("1802")
else:
    print("1")


