"""def test_fun():
    print("hello world")
    test = 2+3+4+5
    print(test)
def cal(num1 , num2 ):
    result = num1+ num2
    print(result)
def better_cal(num1,num2,operator):
    if operator == 'plus':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operator == 'minus':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")


cal(3,5)
cal(4444,6666)
better_cal(5,2,'minus')"""
"""
def greeter(person = 'person', greet= 'hello', weekday='monday') :
    print(f'{person} {greet}')
    print(f"It is a {weekday}")
greeter("koushik", weekday= "Monday")"""
def print_all(first,*arguments,extra):
    print(first)
    print(arguments)
    print(extra)
    for i in arguments:
        print(i)
def print_more(**argument):
    print(argument)

def print_more(*args, **kwargs):
    print(args)
    print(kwargs)




print_all(1,2,3,4,5,55,"HELOO","KALKI",extra=11111)
print_more(arg1 ='1',arg2 = '2', arg3=[1,2,4])
print_more(11,22,33,44,55,555,"HELOO","KALKI",extra=11111)

# exercise
def calculator(*args):
        result = sum(args)
        print(result)
calculator(1,2,3,4,5)