def main():
    name = input("what is your name? ").title()
    hello(name)


def hello(to = "world"):
    print("hello", to)
hello()
main()
