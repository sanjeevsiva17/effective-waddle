# Ex-8
# Read about the module random, it has method randint().
# https://docs.python.org/2/library/random.html
# Create a list with 100 random integers.
# Find out the frequency (how many times each integers is repeated in the list)
# Output should be a dictionary key as the random integer and value is the frequency
# Eg: random_integers_list = [1,2,3,4,1,3,6]
# outputs: frequencies = {1:2, 2:1, 3:2, 4: 1, 6: 1}

from random import randint

# for i in range(100):
#     random_integers.append(randint(0,100))

random_integers = [randint(1, 199000) for i in range(100)]
number_freq = {}

for i in random_integers:
    if i in number_freq:
        number_freq[i] +=1
    else:
        number_freq[i] = 1

        
print("random integers list = ", random_integers)
print("frequencies = ", number_freq)
    
