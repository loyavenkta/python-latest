"""import random
x = random.choice(["head", "tails"])
print(x)
y = random.randint(1,100)
print(y)
z = ["one","two","three"]
random.shuffle(z)
for i in z:
    print(i)"""

""""# statistics doc 
import statistics
print(statistics.mean([30,45]))"""

import sys
"""try:
    print("Hello my name is", sys.argv[1])
except IndexError:
    print("Too feww argument")"""


"""if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("too many argument")"""
""""if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("too many argument")
print("hello, my name is", sys.argv[1])"""

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
for i in sys.argv[1:]:
    print("hello, my name is", i)