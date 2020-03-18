# Ex-6
# Read about the module random, it has method randint().
# https://docs.python.org/2/library/random.html
# Create a list with 100 random integers.

from random import randint

random_integers = [randint(0,100) for i in range(100)]
# for i in range(100):
#     random_integers.append(randint(0,100))

print(random_integers)
