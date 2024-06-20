"""while True:
    n = int(input("what is n?"))
    if n > 0:
        break
for _ in range(n):
    print("meow")"""
def main():
    num = get_number()
    value(num)

def get_number():
    while True:
        n = int(input("whats is n?"))
        if n > 0:
            break
    return n
def value(n):
    for _ in range(n):
        print("LVS")

main()