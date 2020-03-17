# Ex-10
# Write a function isPrime, that takes a number as argument.
# Returns true if it is a prime number, false if it is not.
# Eg: is_prime(20) -> False, is_prime(13) -> True

def isPrime(num):
    if num > 1:             
        for i in range(2, num//2): 
            if (num % i) == 0: 
                return False 
        else: 
            return True

    else: 
        return False

print(isPrime(20))
print(isPrime(13))