# Ex-12
# Write a class Prime.
# It supports the following operations:
# Check out this article to find primes in an optimized way.
# http://stackoverflow.com/a/5813926/2131120

import math

class Prime:
    def isPrime(self, n): 
        if n <= 1: 
            return False
    
        max_div = math.floor(math.sqrt(n))
        for i in range(2, 1 + int(max_div)): 
            if n % i == 0: 
                return False
        return True
        
    def nthprime(self, number):
        curr = 2
        while number:
            if self.isPrime(curr):
                number -=1
            curr+=1
        return curr-1

    def nextprime(self, number):
        number = number + 1
        while number:
            if self.isPrime(number):
                return number
            else:
                number+=1

    def previousprime(self, number):
        number = number - 1
        while number:
            if self.isPrime(number):
                return number
            else:
                number-=1

    def getallprimes(self, number):
        return [i for i in range(number) if self.isPrime(i)]
        

p = Prime()
print(p.nthprime(100)) # prints 100th prime
print(p.nextprime(5)) # 3. It should return 2 for all numbers <= 1
print(p.previousprime(3)) # 2. It should return 2 for all numbers <=2
print(p.getallprimes(10)) # 2, 3, 5, 7