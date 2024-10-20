# Day-4
## 1. generate the prime number within the given range.
```
start = int(input ("Enter the start Value: "))  
end = int(input ("Enter the end Value: "))  
 for number in range (start, end + 1):  
     if number > 1:  
         for i in range (2, number):  
             if (number % i) == 0:  
                 break  
         else:  
             print (number) 
```
Output:- Enter the start Value: 2 <br> Enter the end Value: 11 <br>
2<br>
3<br>
5<br>
7<br>
11

## 2. generate the prime number within the given range using generator. 
```
 def prime_generator(start, end):
     for number in range(start, end + 1):
         if number > 1:
             for i in range(2, int(number**0.5) + 1):  # Check up to the square root
                 if (number % i) == 0:
                     break
             else:
                 yield number  # Yield the prime number

 start = int(input("Enter the start Value: "))  
 end = int(input("Enter the end Value: "))  

 for prime in prime_generator(start, end):
     print(prime)
```
Output:- Enter the start Value: 2 <br> Enter the end Value: 11 <br>
2<br>
3<br>
5<br>
7<br>
11

## 3. generate the prime number within the given range using class.
```
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
```
Output:- Enter the start Value: 2 <br> Enter the end Value: 11 <br>
2<br>
3<br>
5<br>
7<br>
11

## 4. Generate fabonacci number using Generator. 
```
 def fibonacci():
     x, y = 0, 1
     while True:
         yield x
         x, y = y, x + y
 n = int(input("enter the number "))
 print("1st ",n,"Fibonacci numbers:")
 fib = fibonacci()
 for _ in range(n):
     print(next(fib),end=" ")
```
Output:- Enter number: 5 <br>
First 5 Fibonacci numbers:
0 1 1 2 3

## 5. Generate fabonacci number using Class.
```
class Fibonacci:
    @classmethod
    def generate(cls, n):
        x, y = 0, 1
        for _ in range(n):
            print(x, end=' ')
            x, y = y, x + y
n = int(input("Enter number: "))
print(f"First {n} Fibonacci numbers:")
Fibonacci.generate(n)
```
Output:- Enter number: 5 <br>
First 5 Fibonacci numbers:
0 1 1 2 3

## 6. Best time to buy and sell stocks II.
```
def maxProfit(prices):
    # Initialize total maximum profit to 0
    max_profit = 0
    # Start from the second price
    for i in range(1, len(prices)):
        # Check if the current price is greater than the previous price
        if prices[i] > prices[i - 1]:
            # Add the profit from this transaction
            max_profit += prices[i] - prices[i - 1]
    # Return the total maximum profit
    return max_profit
print(maxProfit([1,2,3,4,5])) 
print(maxProfit([7,1,5,3,6,4]))
```
Output:- 4<br>
7
