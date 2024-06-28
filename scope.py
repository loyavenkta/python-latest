"""a = 40
def test_fun():
    print(a)
def test_fun3():
    global a
    a += 2
    print(a)
test_fun()
test_fun3()
"""
# exercise

multipler = 12
has_calculated = True

def multiply_calculated(a):
    global multipler
    global has_calculated
    result = multipler*a
    has_calculated = True
    return result



print(multiply_calculated(2))