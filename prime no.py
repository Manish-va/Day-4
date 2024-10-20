# start = int(input ("Enter the start Value: "))  
# end = int(input ("Enter the end Value: "))  
# for number in range (start, end + 1):  
#     if number > 1:  
#         for i in range (2, number):  
#             if (number % i) == 0:  
#                 break  
#         else:  
#             print (number) 
    

##using class        
class PrimeChecker:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def is_prime(self, num):
        if num <= 1:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                return False

        return True

    def primes_in_range(self):
        primes = []
        for num in range(self.start, self.end + 1):
            if self.is_prime(num):
                primes.append(num)
        return primes
start = int(input("Enter the start value: "))
end = int(input("Enter the end value: "))
checker = PrimeChecker(start, end)
prime_numbers = checker.primes_in_range()
if prime_numbers:
    print(f"Prime numbers between {start} and {end}: {prime_numbers}")
else:
    print(f"There are no prime numbers between {start} and {end}.")

   ## using generator
# def prime_generator(start, end):
#     for number in range(start, end + 1):
#         if number > 1:
#             for i in range(2, int(number**0.5) + 1):  # Check up to the square root
#                 if (number % i) == 0:
#                     break
#             else:
#                 yield number  # Yield the prime number

# start = int(input("Enter the start Value: "))  
# end = int(input("Enter the end Value: "))  

# for prime in prime_generator(start, end):
#     print(prime)
