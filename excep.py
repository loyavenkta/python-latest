"""try:
    print("Hello Koushik")
    x = int(input("whats x? "))
except ValueError:
    print("X is not a integer")
else: 
    print(f"x in {x}")"""
"""while True:
    try:
         print("Hello Koushik")
         x = int(input("whats x? "))
    except ValueError:
         print("X is not a integer")
    else:
         break
print(f"x in {x}")"""
def main():
     x = get_value()
     print(f"x in {x}")

def get_value():
        while True:
            try:
                print("Hello Koushik")
                x = int(input("whats x? "))
            except ValueError:
                pass
                """print("X is not a integer")"""
            else:
                break
        return x
main()

